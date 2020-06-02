from django.db import models

# Create your models here.
class Customer(models.Model):
    class Meta:
        db_table = 'Customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    
    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=50,
    )
    email = models.CharField(
        max_length=50,
        unique=True,
    )
    password = models.CharField(
        max_length=20,
    )

class Orders(models.Model):
    product=models.CharField(
        max_length=50,
    )
    price=models.IntegerField(
        default=0
    )
    date=models.DateField(
        auto_now_add=True,
    )
    customer=models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )