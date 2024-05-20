from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    isadmin=models.CharField(max_length=100,default="NA")
    confirm_password=models.CharField(max_length=100,blank=True)


class details(models.Model):
    id_cust=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Status=models.CharField(max_length=100,null=True)
    date_1=models.DateTimeField(auto_now=True)
    Rack_Location = models.CharField(max_length=100,null=True)  # Add this field
    Ip=models.CharField(max_length=100,null=True) # Add this field
    def __str__(self):
        return self.Ip
class live_data(models.Model):
    ip_address = models.GenericIPAddressField()
    status = models.CharField(max_length=100)  # Add this field
    timestamp = models.DateTimeField(auto_now_add=True)
    cust_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.ip_address
    

class csv_1(models.Model):
    
    Ip= models.CharField(max_length=100)  # Add this field
    Location = models.CharField(max_length=100)
    Description = models.CharField(max_length=300,null=True)
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    