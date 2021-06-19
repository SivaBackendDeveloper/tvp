import os

from django.db import models
# Create your models here.


class Member(models.Model):
 name=models.CharField(max_length=100)
 role=models.CharField(max_length=100)
 mobilenumber=models.BigIntegerField()


import datetime
def get_file_path(request, filename):
    filename_original = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, filename_original)
    return os.path.join('image/', filename)

class Activity(models.Model):
 date=models.DateField()
 activity=models.CharField(max_length=1000)
 image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
 responce=models.CharField(max_length=100)
