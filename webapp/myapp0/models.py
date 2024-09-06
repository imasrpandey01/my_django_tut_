from django.db import models

# Create your models here.

class Employee(models.Model):
    e_no=models.IntegerField()
    e_name=models.CharField(max_length=64)
    e_salary=models.IntegerField()
    e_addr=models.CharField(max_length=64)
    

    
