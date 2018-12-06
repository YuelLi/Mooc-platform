from datetime import datetime

from django.db import models
# Create your models here.


class Course(models.Model):
    name=models.CharField(max_length=50,verbose_name="course name")
    desc=models.CharField(max_length=50,verbose_name="course description")
    detail=models.TextField(verbose_name="course detail")
    degree=models.CharField(choices=(("el","elementary"),("in","intermediate"),("ad","advanced")),max_length=2)
    study_time=models.IntegerField(default=0, verbose_name="study time in minutes")
    student_nums=models.IntegerField(default=0, verbose_name="student numbers")
    favor_nums=models.IntegerField(default=0, verbose_name="favor numbers")
    image=models.ImageField(upload_to="courses/%Y/%m",verbose_name="cover image",max_length=100)
    click_nums=models.IntegerField(default=0,verbose_name="click numbers")
    add_time= models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name="course"
        verbose_name_plural="courses"


class Lesson(models.Model):
    course= models.ForeignKey(Course, verbose_name="course",on_delete=models.CASCADE)
    name=models.CharField(max_length=100, verbose_name="lesson name")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="add time")

    class Meta:
        verbose_name="lesson"
        verbose_name_plural="lessons"


class Video(models.Model):
    lesson = models.ForeignKey(Course, verbose_name="lesson",on_delete=models.CASCADE)
    name=models.CharField(max_length=100, verbose_name="video name")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="add time")


    class Meta:
        verbose_name="video"
        verbose_name_plural="videos"


class CourseResource(models.Model):
    course=models.ForeignKey(Course, verbose_name="course",on_delete=models.CASCADE)
    name=models.CharField(max_length=100, verbose_name="course resource name")
    download=models.FileField(upload_to="courses/resources/%Y/%m",verbose_name="resource file",max_length=100)
    add_time=models.DateTimeField(default=datetime.now,verbose_name="add time")


    class Meta:
        verbose_name="course resource"
        verbose_name_plural="course resources"