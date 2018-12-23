from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,default="")
    birthday = models.DateField(null=True, blank=True)
    gender =models.CharField(max_length=2,choices=(("m","male"),("f","female")),default="f")
    address =models.CharField(max_length=100, default="")
    mobile=models.CharField(max_length=10, null=True, blank=True)
    image=models.ImageField(upload_to="image/%Y/%m",default="image/default.png", max_length=100)

    class Meta:
        verbose_name="user information"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name="Verification code")
    email = models.EmailField(max_length=50, verbose_name="Email address")
    send_type=models.CharField(choices=(("r","Register"),("f","Forget password")),max_length=2,verbose_name="Type")
    send_time=models.DateTimeField(default=datetime.now,verbose_name="Time")

    class Meta:
        verbose_name= "Email verification"
        verbose_name_plural=verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code,self.email)

class Banner(models.Model):
    title =models.CharField(max_length=100, verbose_name="Title")
    image =models.ImageField(upload_to="banner/%Y/%m",verbose_name="Image",max_length=100)
    url= models.URLField(max_length=200, verbose_name="Url")
    index=models.IntegerField(default=100)
    add_time=models.DateTimeField(default=datetime.now, verbose_name="Time")

    class Meta:
        verbose_name= "banner"
        verbose_name_plural="banners"
