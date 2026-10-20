from django.db import models

class Part(models.Model):
    CATEGORY_CHOICES = [
        ("CPU", "CPU"),
        ("GPU", "GPU"),
        ("MOBO", "Motherboard"),
        ("RAM", "RAM"),
        ("STORAGE", "Storage"),
        ("PSU", "Power Supply"),
        ("CASE", "Case"),
        ("COOLER", "Cooler"),
        ("OTHER", "Other"),
    ]
    
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    build = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"