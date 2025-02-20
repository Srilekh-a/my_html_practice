from django.db import models

# Create your models here.
class student1(models.Model):
    std_name=models.CharField(max_length=50)
    std_lastname=models.CharField(max_length=50)
    std_address=models.CharField(max_length=50)
    def __str__(self):
        return self.std_name

