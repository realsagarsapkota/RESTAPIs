from django.db import models
from django.utils import timezone
# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_joined = models.DateField(auto_now_add=timezone.now())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    