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

    def __str__(self):
        return self.name

class CourseOrg(models.Model):
    name= models.CharField(max_length=50, verbose_name="Organization Name")
    desc= models.TextField(verbose_name="Description")
    category= models.CharField(max_length=10,default="school",choices=(("1","Training institution"),("2","School"),("3","Individual")),verbose_name="Category")
    click_num= models.IntegerField(default=0, verbose_name="Flick number")
    fav_num = models.IntegerField(default=0, verbose_name="Favorites number")
    student_num=models.IntegerField(default=0, verbose_name="Student number")
    course_num = models.IntegerField(default=0, verbose_name="Course number")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="Image", max_length=100)
    address =models.CharField(max_length=150, verbose_name="Organization Address")
    city =models.ForeignKey(CityDict, verbose_name="Located City",on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name="Course Organization"
        verbose_name_plural="Course Organizations"

    def __str__(self):
        return self.name

class Instructor(models.Model):
    org =models.ForeignKey(CourseOrg,verbose_name="Organization at", on_delete=models.CASCADE)
    name=models.CharField(max_length=50, verbose_name="Instructor Name")
    image=models.ImageField(default='',upload_to="instructor/%Y/%m", verbose_name="Image")
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

    def __str__(self):
        return self.name