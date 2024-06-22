from django.db import models

class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=500)
    replay = models.CharField(max_length=500)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'complaint'


