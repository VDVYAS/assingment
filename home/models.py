from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userInfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    order_date=models.DateField()
    company_name= models.TextField(max_length=100)
    owner=models.CharField(max_length=100)
    item=models.CharField(max_length=100)
    quantity=models.IntegerField(null=True)
    weight=models.FloatField(null=True)
    req_of_shpment=models.CharField(max_length=100)
    tracking_id=models.CharField(max_length=100)
    shipment_size=models.CharField(max_length=100)
    box_count=models.IntegerField(null=True)
    specification=models.CharField(max_length=100)
    checklist_quantity=models.CharField(max_length=100)

    #@staticmethod
    #def get_all_product_coustomer1():
     #   return userInfo.objects.filter(user="vd")
    #@staticmethod
    #def get_all_product_coustomer2():
     #   return userInfo.objects.filter(user="vd1")