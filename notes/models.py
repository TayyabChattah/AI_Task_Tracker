from django.db import models

# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    category=models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.title