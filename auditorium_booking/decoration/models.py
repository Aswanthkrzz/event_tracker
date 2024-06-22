from django.db import models

# Create your models here.
class Decoration(models.Model):
    d_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=1000)
    finction_id = models.CharField(max_length=100)
    price = models.IntegerField()
    discription = models.CharField(max_length=200)
    place = models.CharField(max_length=100)
    event_team_name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'decoration'

