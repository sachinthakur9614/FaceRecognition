from django.db import models

# Create your models here.


class AddSku(models.Model):
	serviceName = models.CharField(max_length=50)

