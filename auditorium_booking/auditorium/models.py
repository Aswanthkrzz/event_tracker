from django.db import models
from user.models import User

# Create your models here.
class Auditorium(models.Model):
    aud_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    amount = models.CharField(max_length=30)
    d_id = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    services = models.CharField(max_length=500)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'auditorium'

class AuditoriumFeedback(models.Model):
    af_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    # u_id = models.IntegerField()
    u=models.ForeignKey(User,to_field='u_id',on_delete=models.CASCADE)
    aud_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auditorium_feedback'



