from django.db import models


class PhoneCatalog(models.Model):
    Name = models.CharField(max_length=255)
    Pub_date = models.DateTimeField('registration date')
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=30)

# Create your models here.
