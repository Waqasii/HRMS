from django.db import models

# Create your models here.
class Manager(models.Model):
    name=models.TextField(blank=False,max_length=250)
    email=models.EmailField(blank=False)
    cnic=models.TextField(blank=False,max_length=15,primary_key=True)
    
    def __str__(self):
        return self.name