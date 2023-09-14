from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Contact(models.Model):
    SIno =models.AutoField(primary_key=True)
    Name=models.CharField(max_length=70)
    Phone=models.CharField(max_length=13)
    Email=models.CharField(max_length=30)
    Content=models.TextField(max_length=400)
    time= models.DateTimeField(default=now)
    # time=models.DateTimeField(auto_now_add=True,blank=True)


    def __str__(self):
        return "From "+ self.Name + " " + "-"+ " "+self.Email

class Post(models.Model):
    SIno=models.AutoField(primary_key=True)# automatically complete fields 
    Author=models.CharField(max_length=50)
    Email=models.CharField(max_length=30)
    Title=models.CharField(max_length=70)
    slug=models.CharField(max_length=150)
    Content=models.TextField()
    time= models.DateTimeField(default=now)
    # time=models.DateTimeField(blank=True)

    def __str__(self):
        return "From "+self.Author+" - "+self.Title 
    
class PostComments(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    time= models.DateTimeField(default=now)
