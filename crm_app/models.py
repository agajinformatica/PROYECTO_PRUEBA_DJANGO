from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo personalizado de usuario basado en AbstractUser
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name() or self.username

# Empresa a la que pertenece el cliente
class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Cliente asociado a una empresa y a un representante de ventas
class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    representative = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

# Interacción con el cliente (ej. llamada, correo, etc.)
class Interaction(models.Model):
    INTERACTION_CHOICES = [
        ('Call', 'Call'),
        ('Email', 'Email'),
        ('SMS', 'SMS'),
        ('Facebook', 'Facebook'),
        ('WhatsApp', 'WhatsApp'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50, choices=INTERACTION_CHOICES)
    interaction_date = models.DateTimeField()

    def __str__(self):
        return f"{self.customer.full_name} - {self.interaction_type}"
