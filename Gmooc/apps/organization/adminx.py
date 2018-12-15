import xadmin

from .models import CityDict, CourseOrg, Instructor

class CityDictAdmin(object):
    list_display = ['name','desc','add_time']
    search_fields= ['name','desc']
    list_filter= ['name','desc','add_time']

class CourseOrgAdmin(object):
    list_display = ['name','desc','address','city','fav_num','click_num','image','add_time']
    search_fields= ['name','desc','address','city','fav_num','click_num']
    list_filter= ['name','desc','address','city','fav_num','click_num','add_time']

class InstructorAdmin:
    list_display = ['org','name','work_year','company','position','feature','click_num','fav_num','add_time']
    search_fields= ['org','name','work_year','company','position','feature','click_num','fav_num']
    list_filter= ['org','name','work_year','company','position','feature','click_num','fav_num','add_time']

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Instructor,InstructorAdmin)