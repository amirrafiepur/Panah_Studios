from django.db import models
from webb.models import Human

class category(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return  self.name
    
class tags(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class comments(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()   
    def __str__(self):
        return self.name 

class post(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated =models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    counted_views = models.IntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.BinaryField()
    author = models.ForeignKey(Human,on_delete=models.CASCADE,null=True)
    post_category = models.ForeignKey(category,on_delete=models.PROTECT,null=True)
    tag = models.ForeignKey(tags,on_delete=models.PROTECT,null=True)
    comment = models.ForeignKey(comments,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title