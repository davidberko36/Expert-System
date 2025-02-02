from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
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
