from django.db import models
from auditorium.models import Auditorium
from vender.models import Vender



class Order(models.Model):
    ap_id = models.AutoField(primary_key=True)
    u_id = models.IntegerField()
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    amount = models.IntegerField()
    payment = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10)
    # aud_id = models.IntegerField()
    aud = models.ForeignKey(Auditorium, to_field='aud_id', on_delete=models.CASCADE)
    # vend_id = models.IntegerField()
    vend=models.ForeignKey(Vender,to_field='vend_id',on_delete=models.CASCADE)
    program = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'order'




