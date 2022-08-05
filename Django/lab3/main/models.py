from django.db import models

# Create your models here.

class costomers(models.Model):
	name = models.CharField(max_length=50)
	surename = models.CharField(max_length=50)
	username = models.CharField(max_length=50, unique=True)


class costomer(models.Model):
	name = models.CharField(max_length=50)
	surename = models.CharField(max_length=50)
	username = models.CharField(max_length=50, unique=True)


class comentator(models.Model):
	username = models.CharField(max_length=50, unique=True)
	comment = models.CharField(max_length=200)
	commen_mac = models.CharField(max_length=200, default=True)
	datepub = models.DateTimeField(auto_now_add=True)
