from django.db import models
from django.core import validators as v
# Create your models here.
class Employees(models.Model):
    DEPARTMENT = (
        ('HR', 'Human Resource'),
        ('ST', 'Software Testing'),
        ('JD', 'Junior Developer')
    )
    name = models.CharField(
        max_length=50,
        verbose_name = "User Name",
        validators=[
            v.MinLengthValidator(3),
            v.MinLengthValidator(30),
        ]
    )

    emp_age = models.IntegerField(
        name = "age",
        verbose_name="Age",
        default=0,
        validators=[
            v.MinValueValidator(20, "Invalid age"),
            v.MaxValueValidator(70, "Invalid age")
        ]
    )
    department = models.CharField(
        max_length = 50,
        choices=DEPARTMENT,
        default = 'HR'
    )
