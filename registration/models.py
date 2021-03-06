from django.db import models

# Create your models here.
class region(models.Model):
    location       = models.CharField(max_length=20, null=False)
   

    def __str__(self):
        return self.location 

class profession(models.Model):
    pro_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70, null=False, blank=False)
    def __str__(self):
        return self.name


class user(models.Model):
    user_id  = models.BigAutoField(primary_key=True)
    fname    = models.CharField(max_length=20)
    lname    = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20)
    user_name= models.CharField(max_length=30, blank=True, null=True, unique=True)
    email    = models.EmailField()
    passwd   = models.CharField(max_length=50, null='False')
    age      = models.CharField(max_length=4)
    slug     = models.CharField(max_length=30, unique=True)
    time     = models.TimeField(auto_now=True)
    date     = models.DateField(auto_now=True)
    image    = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    location = models.ForeignKey(region, on_delete=models.CASCADE)
    prfssn   = models.ForeignKey(profession, on_delete=models.CASCADE)
    description=models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f'{self.fname} - {self.lname}'