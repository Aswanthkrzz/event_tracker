from django.db import models

# Create your models here.
class Event(models.Model):
    e_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    adress = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'event'
