from django.db import models
from user.models import User
# Create your models here.
class Feedback(models.Model):
    f_id = models.AutoField(primary_key=True)
    u_id = models.IntegerField()
    # u=models.ForeignKey()
    feedback = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'feedback'
