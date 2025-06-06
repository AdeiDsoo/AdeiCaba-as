from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    size = models.CharField(max_length=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_created = models.DateField(null=True)
    image=models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return self.name
