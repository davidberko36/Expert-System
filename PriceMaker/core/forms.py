# from django import forms
# from .models import Product

# class ProductForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Add Bootstrap classes to all fields
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'

#     class Meta:
#         model = Product
#         fields = [
#             "name",
#             "base_cost",
#             "competitor_price",
#             "market_demand",
#             "customer_wtp",
#             "is_seasonal",
#             "profit_margin",
#         ]
        


from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        # Explicitly define is_seasonal as a checkbox with Bootstrap styling
        self.fields["is_seasonal"].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})

    class Meta:
        model = Product
        fields = [
            "name",
            "base_cost",
            "competitor_price",
            "market_demand",
            "customer_wtp",
            "is_seasonal",
            "profit_margin",
        ]
