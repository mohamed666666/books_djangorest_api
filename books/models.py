from django.db import models
import uuid
from django.conf import settings

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=100)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="product_creator",on_delete=models.CASCADE)



class Pages(models.Model):
    number=models.IntegerField()
    content=models.CharField(max_length=10000)
    book=models.ForeignKey(Books,related_name='books',on_delete=models.CASCADE)



    

