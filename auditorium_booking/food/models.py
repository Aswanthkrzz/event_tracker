from django.db import models

# Create your models here.

class Food(models.Model):
    f_if = models.AutoField(primary_key=True)
    image = models.CharField(max_length=500)
    food_id = models.CharField(max_length=100)
    price = models.IntegerField()
    discription = models.CharField(max_length=500)
    place = models.CharField(max_length=100)
    event_team_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'food'
