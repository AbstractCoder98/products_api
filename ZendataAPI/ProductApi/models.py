from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=500)
    description = models.CharField(blank=True, max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
