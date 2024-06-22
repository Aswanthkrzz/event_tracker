from django.db import models
from user.models import User

# Create your models here.
class Vender(models.Model):
    vend_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    u_id = models.IntegerField()
    status = models.CharField(max_length=20)
    lisence_id = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    # amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vender'


class EventFeedback(models.Model):
    f_id = models.AutoField(primary_key=True)
    # u_id = models.IntegerField()
    u=models.ForeignKey(User,to_field='u_id',on_delete=models.CASCADE)
    feedback = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    vend_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_feedback'


