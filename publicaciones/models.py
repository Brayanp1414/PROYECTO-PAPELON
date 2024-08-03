from django.db import models

# Create your models here.
class tabla1(models.Model):
    titulo=models.CharField(max_length=20, default=True)
    descripcion=models.TextField(default=True)

