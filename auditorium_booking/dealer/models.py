from django.db import models

# Create your models here.
class Dealer(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=50)
    d_address = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    status = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'dealer'
