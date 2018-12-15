from django.db import models
from datetime import datetime
# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name="City Name")
    desc =models.CharField(max_length=200, verbose_name="City Description")
    add_time =models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name="City"
        verbose_name_plural="Cities"

class CourseOrg(models.Model):
    name= models.CharField(max_length=50, verbose_name="Organization Name")
    desc= models.CharField(max_length=200,verbose_name="Organization")
    click_num= models.IntegerField(default=0, verbose_name="click number")
    fav_num = models.IntegerField(default=0, verbose_name="favorites number")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="cover image", max_length=100)
    address =models.CharField(max_length=150, verbose_name="Organization Address")
    city =models.ForeignKey(CityDict, verbose_name="Located City",on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name="Course Organization"
        verbose_name_plural="Course Organizations"

class Instructor(models.Model):
    org =models.ForeignKey(CourseOrg,verbose_name="Organization at", on_delete=models.CASCADE)
    name=models.CharField(max_length=50, verbose_name="Instructor Name")
    work_year = models.IntegerField(default=0, verbose_name="work years")
    company =models.CharField(max_length=50, verbose_name="company works for")
    position= models.CharField(max_length=50, verbose_name="position")
    feature =models.CharField(max_length=50, verbose_name="teaching feature")
    click_num = models.IntegerField(default=0, verbose_name="click number")
    fav_num = models.IntegerField(default=0, verbose_name="favorite number")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"