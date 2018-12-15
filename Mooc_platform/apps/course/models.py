from datetime import datetime

from django.db import models
# Create your models here.


class Course(models.Model):
    name=models.CharField(max_length=50,verbose_name="Course name")
    desc=models.CharField(max_length=50,verbose_name="Course description")
    detail=models.TextField(verbose_name="Course detail")
    difficulty=models.CharField(choices=(("el","Elementary"),("in","Intermediate"),("ad","Advanced")),max_length=2,verbose_name="Difficulty")
    study_time=models.IntegerField(default=0, verbose_name="Study time (min)")
    student_num=models.IntegerField(default=0, verbose_name="Student number")
    favor_num=models.IntegerField(default=0, verbose_name="Favor number")
    image=models.ImageField(upload_to="courses/%Y/%m",verbose_name="Cover image",max_length=100)
    click_num=models.IntegerField(default=0,verbose_name="Click number")
    add_time= models.DateTimeField(default=datetime.now, verbose_name="Add time")

    class Meta:
        verbose_name="Course"
        verbose_name_plural="Courses"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course= models.ForeignKey(Course, verbose_name="Course",on_delete=models.CASCADE)
    name=models.CharField(max_length=100, verbose_name="Lesson name")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="Add time")

    class Meta:
        verbose_name="Lesson"
        verbose_name_plural="Lessons"


class Video(models.Model):
    lesson = models.ForeignKey(Course, verbose_name="Lesson",on_delete=models.CASCADE)
    name=models.CharField(max_length=100, verbose_name="Video name")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="Add time")


    class Meta:
        verbose_name="Video"
        verbose_name_plural="Videos"


class CourseResource(models.Model):
    course=models.ForeignKey(Course, verbose_name="Course",on_delete=models.CASCADE)
    name=models.CharField(max_length=100, verbose_name="Course resource name")
    download=models.FileField(upload_to="courses/resources/%Y/%m",verbose_name="Resource file",max_length=100)
    add_time=models.DateTimeField(default=datetime.now,verbose_name="Add time")


    class Meta:
        verbose_name="Course resource"
        verbose_name_plural="Course resources"