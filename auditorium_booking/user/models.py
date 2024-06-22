from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    place = models.CharField(max_length=40)
    u_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'
