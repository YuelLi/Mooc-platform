from datetime import datetime

from django.db import models

from user.models import UserProfile
from course.models import Course
# Create your models here.
class UserConsult(models.Model):
    name = models.CharField(max_length=50, verbose_name="Username")
    mobile= models.CharField(max_length=10, verbose_name="Phone Number")
    course_name =models.CharField(max_length=50, verbose_name="Course Name")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name="User Consultation"
        verbose_name_plural="User Consultations"


class CourseComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="User",on_delete=models.CASCADE)
    course= models.ForeignKey(Course,verbose_name="Course",on_delete=models.CASCADE)
    comment= models.CharField(max_length=200,verbose_name="Comment")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="add time")

    class Meta:
        verbose_name="Course Comment"
        verbose_name_plural="Course Comments"

class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="User", on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0, verbose_name="Favorite ID")
    fav_type= models.IntegerField(choices=((1,"course"),(2,"organization"),(3,"instructor")), default=1, verbose_name="favorite type")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name="User Favorite"
        verbose_name_plural="User Favorites"

class UserMessage(models.Model):
    user=models.IntegerField(default=0, verbose_name="User ID")
    message = models.CharField(max_length=500, verbose_name="Message Content")
    is_read= models.BooleanField(default=False)
    add_time=models.DateTimeField(default=datetime.now,verbose_name="add time")

    class Meta:
        verbose_name="User Message"
        verbose_name_plural="User Messages"


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="User",on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name="Course",on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name ="User Course"
        verbose_name_plural="User Courses"
