from django.db import models
from event.models import Event

# Create your models here.
class Payment(models.Model):
    amount = models.FloatField()
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    provider_order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    signatur_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'payment'
