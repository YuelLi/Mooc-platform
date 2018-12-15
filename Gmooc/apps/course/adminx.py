import xadmin

from .models import Course,Lesson, Video, CourseResource

class CourseAdmin(object):
    list_display = ['name','desc','detail','difficulty','study_time','student_num','favor_num','image','click_num','add_time']
    search_fields= ['name','desc','detail','difficulty','study_time','student_num','favor_num','click_num']
    list_filter= ['name','desc','detail','difficulty','study_time','student_num','favor_num','click_num','add_time']

class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields= ['course','name']
    list_filter= ['course__name','name','add_time']

class VideoAdmin:
    list_display = ['lesson','name','add_time']
    search_fields= ['lesson','name']
    list_filter= ['lesson','name','add_time']

class CourseResourceAdmin:
    list_display = ['course','name','download','add_time']
    search_fields= ['course','name','download']
    list_filter= ['course','name','download','add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)