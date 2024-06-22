from django.db import models
from user.models import User
from photography.models import Photography

# Create your models here.
class Photobook(models.Model):
    f_id = models.AutoField(primary_key=True)
    date = models.DateField()
    place = models.CharField(max_length=10)
    # u_id = models.IntegerField()
    u=models.ForeignKey(User,to_field='u_id',on_delete=models.ForeignKey)
    time = models.TimeField()
    status = models.CharField(max_length=20)
    service = models.CharField(max_length=100)
    # ph_id = models.IntegerField()
    ph=models.ForeignKey(Photography,to_field='ph_id',on_delete=models.ForeignKey)

    class Meta:
        managed = False
        db_table = 'photobook'

