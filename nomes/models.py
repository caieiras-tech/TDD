from django.db import models

# Create your models here.

class Nome(models.Model):
    nome = models.CharField(max_length=255)