from pydoc import describe
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=20)
    description= models.TextField()


class Ledger(models.Model):
    name = models.CharField(max_length=20)
    expenditure=models.BooleanField(default=True)
    description= models.TextField()
    userLikeList = models.ManyToManyField(Account, through='TransactionRecord', related_name='AccountLedger')

class TransactionRecord(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    ledger = models.ForeignKey(Ledger, on_delete=models.PROTECT)
    money = models.IntegerField()

