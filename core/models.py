from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Item(models.Model):
    merchant=models.ForeignKey(Profile,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    comment=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images')
    price_range=models.CharField(max_length=200)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name+" by "+self.merchant.user.username

    class Meta:
        ordering=["-created_on"]
