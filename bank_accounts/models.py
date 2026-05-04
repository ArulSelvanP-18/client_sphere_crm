from django.db import models
import random
from datetime import datetime

class Account(models.Model):
    account_number = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default='Active')

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = str(random.randint(100000000000, 999999999999))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Deposit', 'Deposit'),
        ('Withdrawal', 'Withdrawal'),
        ('Transfer', 'Transfer'),
    ]
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.account.name} - {self.type} - ₹{self.amount}"