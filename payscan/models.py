from django.contrib.auth.models import User
from django.db import models

class PayscanUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.user}'

class Business(models.Model):
    owner = models.OneToOneField(PayscanUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.name} {self.owner} {self.balance}'

class Transaction(models.Model):
    payer = models.ForeignKey(PayscanUser, on_delete=models.CASCADE, related_name='payer')
    payee = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='payee',null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=20) 

    def __str__(self):
        return f'{self.payer}" - " {self.payee} " - "{self.amount}" - "{self.timestamp}" - "{self.transaction_type}'
