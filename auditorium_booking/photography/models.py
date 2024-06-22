from django.db import models
from user.models import User
# Create your models here.

class Photography(models.Model):
    ph_id = models.AutoField(primary_key=True)
    studio_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    rate_photo = models.IntegerField()
    rate_video = models.IntegerField()
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'photography'
class PhotoFeedback(models.Model):
    pf_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    ph_id = models.IntegerField()
    # u_id = models.IntegerField()
    u=models.ForeignKey(User,to_field='u_id',on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'photo_feedback'

