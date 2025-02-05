from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .bridge import PriceEngine
from .models import Product, PriceHistory
# Create your views here.

def calculate_price(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            engine = PriceEngine()
            result = engine.calculate_price(product)  # Pass model instance

            if result:
                product.current_price = result['price']
                product.save()
                PriceHistory.objects.create(
                    product = product,
                    suggested_price = result['price'],
                    reasoning = result['reasoning'],
                    potential_risks = "Market analysis required"
                )

                return redirect('price_detail', pk=product.pk)
    else:
        form = ProductForm()

    return render(request, 'core/calculate_price.html', {'form': form})


def price_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    price_history = PriceHistory.objects.filter(product=product).first()
    return render(request, 'core/price_detail.html', {
        'product': product,
        'price_history': price_history
    })