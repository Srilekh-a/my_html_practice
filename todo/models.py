from django.db import models

# Create your models here.
class list(models.Model):
    title=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=True)

    def __str__(self):
        return self.title 

