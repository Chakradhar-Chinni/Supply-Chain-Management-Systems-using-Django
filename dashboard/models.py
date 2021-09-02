from django.db import models

# Create your models here.
class AdminRegistration(models.Model):
    Name   = models.CharField(max_length=100,blank=False)
    UserName = models.CharField(max_length=100,blank=False)
    ContactNo = models.CharField(max_length=100,blank=False)
    Email = models.CharField(max_length=100,blank=False)
    Password = models.CharField(max_length=100,blank=True)
    temp = models.CharField(max_length=100,blank=True) 
    class Meta:
        db_table = "adminreg_table"

class UserRegistration(models.Model):
    Name   = models.CharField(max_length=100,blank=False)
    UserName = models.CharField(max_length=100,blank=False) 
    ContactNo = models.CharField(max_length=100,blank=False)
    Email = models.CharField(max_length=100,blank=False)
    Password = models.CharField(max_length=100,blank=False)
    class Meta:
        db_table = "userreg_table"

class SupplierRegistration(models.Model):
    Name   = models.CharField(max_length=100,blank=False)
    UserName = models.CharField(max_length=100,blank=False)
    ContactNo = models.CharField(max_length=100,blank=False)
    Email = models.CharField(max_length=100,blank=False)
    Password = models.CharField(max_length=100,blank=False)
    class Meta:
        db_table = "supplierreg_table"  
  
class UserOrder(models.Model):
    ProductName = models.CharField(max_length=100,blank=False)
    Quantity = models.CharField(max_length=100,blank=False)
    states = (('Andhra Pradesh','Andhra Pradesh'),('Telangana','Telangana'),('Tamil Nadu','Tamil Nadu'),(('Karnataka','Karnataka')))
    State = models.CharField(max_length=100,choices=states,blank=False)
    SupplierId = models.IntegerField(default=-1)
    UserId = models.IntegerField(default=-1)
    OrderStatus = models.CharField(max_length=100,blank=False,default='In-Progress')
    SupplierStatus = models.CharField(max_length=100,blank=False,default='Not Assigned')
    class Meta:
        db_table = "userorder_table"

class tud(models.Model):
    UserName = models.CharField(max_length=100,blank=False)
    Number   = models.CharField(max_length=100,blank=False)
    Status   = models.CharField(max_length=100,blank=False,default='In-Progress')
    category_choices = (('Education','Education'),('Programming','Programming'),('Others','Others'))
    category = models.CharField(max_length=100,choices=category_choices,blank=False)
    class Meta:
        db_table = "tud_table"

class tmd(models.Model):
    UserName = models.CharField(max_length=100,blank=False)
    Number   = models.CharField(max_length=100,blank=False)
    class Meta:
        db_table = "tmd_table"