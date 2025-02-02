from django.db import models

# Create your models here.
class Product(models.Model):
    DEMAND_CHOICES = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]

    WTP_CHOICES = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]
    
    name = models.CharField(max_length=100)
    base_cost = models.DecimalField(max_digits=10, decimal_places=2)
    competitor_price = models.DecimalField(max_digits=10, decimal_places=2)
    market_demand = models.CharField(max_length=6, choices=DEMAND_CHOICES)
    customer_wtp = models.CharField(max_length=6, choices=WTP_CHOICES)
    is_seasonal = models.BooleanField(default=False)
    profit_margin = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    

class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    suggested_price = models.DecimalField(max_digits=10, decimal_places=2)
    reasoning = models.TextField()
    potential_risks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    