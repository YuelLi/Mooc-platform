from datetime import datetime

from django.db import models
from organization.models import CourseOrg, Instructor
# Create your models here.


class Course(models.Model):
    name=models.CharField(max_length=50,verbose_name="Course name")
    course_org=models.ForeignKey(CourseOrg, verbose_name="Organization", on_delete=models.CASCADE)
    desc=models.CharField(max_length=50,verbose_name="Course description")
    detail=models.TextField(verbose_name="Course detail")
    instructor=models.ForeignKey(Instructor, verbose_name="Instructor", on_delete=models.CASCADE)
    requisite =models.CharField(default="", max_length=200, verbose_name="requisite")
    objective = models.CharField(default="", max_length=200, verbose_name="objective")
    difficulty=models.CharField(choices=(("el","Elementary"),("in","Intermediate"),("ad","Advanced")),max_length=2,verbose_name="Difficulty")
    study_time=models.IntegerField(default=0, verbose_name="Study time (min)")
    student_num=models.IntegerField(default=0, verbose_name="Student number")
    favor_num=models.IntegerField(default=0, verbose_name="Favor number")
    image=models.ImageField(upload_to="courses/%Y/%m",verbose_name="Cover image",max_length=100)
    click_num=models.IntegerField(default=0,verbose_name="Click number")
    category =models.CharField(default="",max_length=20, verbose_name="Category")
    tag= models.CharField(default="", max_length=20, verbose_name="tag")
    add_time= models.DateTimeField(default=datetime.now, verbose_name="Add time")

    class Meta:
        verbose_name="Course"
        verbose_name_plural="Courses"

    def get_lessons(self):
        return self.lesson_set.all()

    def __str__(self):
        return self.name



class Lesson(models.Model):
    course= models.ForeignKey(Course, verbose_name="Course",on_delete=models.CASCADE)
    name=models.CharField(max_length=100, verbose_name="Lesson name")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="Add time")

    class Meta:
        verbose_name="Lesson"
        verbose_name_plural="Lessons"

    def get_videos(self):
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="Lesson",on_delete=models.CASCADE)
    name=models.CharField(max_length=100, verbose_name="Video name")
    url =models.CharField(default="", max_length=200,verbose_name="URL")
    study_time = models.IntegerField(default=0, verbose_name="Study time (min)")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="Add time")

    class Meta:
        verbose_name="Video"
        verbose_name_plural="Videos"

    def __str__(self):
        return self.name

class CourseResource(models.Model):
    course=models.ForeignKey(Course, verbose_name="Course",on_delete=models.CASCADE)
    name=models.CharField(max_length=100, verbose_name="Course resource name")
    download=models.FileField(upload_to="courses/resources/%Y/%m",verbose_name="Resource file",max_length=100)
    add_time=models.DateTimeField(default=datetime.now,verbose_name="Add time")


    class Meta:
        verbose_name="Course resource"
        verbose_name_plural="Course resources"

    def __str__(self):
        return self.name