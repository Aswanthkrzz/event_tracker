from django.db import models
from auditorium.models import Auditorium
from user.models import User
from event.models import Event
# Create your models here.
class Booking(models.Model):
    ab_id = models.AutoField(primary_key=True)
    # aud_id = models.IntegerField()
    aud=models.ForeignKey(Auditorium,to_field='aud_id',on_delete=models.CASCADE)
    # u_id = models.IntegerField()
    u=models.ForeignKey(User,to_field='u_id',on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    no_of_days = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    booking_time = models.CharField(max_length=500)
    fecilities = models.CharField(max_length=40)
    floors = models.CharField(max_length=40)
    occasion = models.CharField(max_length=100)
    e_id = models.IntegerField()
    vend_id = models.IntegerField()
    amount = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'booking'

