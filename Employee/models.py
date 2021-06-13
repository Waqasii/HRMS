from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.TextField(primary_key=True,blank=False,unique=True)
    
    def __str__(self):
        return str(self.name)
    
    
class Employee(models.Model):
    name=models.TextField(blank=False,max_length=250)
    email=models.EmailField(blank=False)
    cnic=models.TextField(primary_key=True,blank=False,max_length=15)
    department=models.ForeignKey('Department',on_delete = models.CASCADE)
    image=models.ImageField(upload_to='upload/',blank=False)
    
    
    def __str__(self):
        return str(self.name)
    


