from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Course, CourseResource, Video
from operation.models import UserFavorite, UserCourse, CourseComment
from utils.utils import LoginRequiredMixin
# Create your views here.

class CourseListView(View):
    def get(self, request):
        all_courses= Course.objects.all().order_by("-add_time")
        recommended_course= Course.objects.all().order_by("-click_num")[:3]
        sort=request.GET.get('sort','')
        if sort:
            if sort=="popular":
                all_courses=all_courses.order_by("-click_num")
            elif sort=="enrolled":
                all_courses=all_courses.order_by("-student_num")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        org_paginator = Paginator(all_courses, 3, request=request)
        courses = org_paginator.page(page)
        return render(request,'course-list.html',{
            'all_courses':courses,
            'recommended_course':recommended_course,
            'sort':sort,
        })


class CourseDetailView(View):
    def get(self,request, course_id):
        course=Course.objects.get(id=course_id)
        course.click_num+=1
        course.save()
        is_course_favored=False
        is_org_favored=False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user,fav_id= course_id, fav_type=1):
                is_course_favored=True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                is_org_favored=True
        tag =course.tag
        if tag:
            related_courses= Course.objects.filter(Q(tag=tag) & ~Q(id=course_id))[:2]
        else:
            related_courses=[]
        return render(request, 'course-detail.html' ,{
            'course':course,
            'related_courses':related_courses,
            'is_course_favored':is_course_favored,
            'is_org_favored':is_org_favored,
        })



class CourseInfoView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course=Course.objects.get(id=course_id)
        #check if user is already connected this course
        user_courses=UserCourse.objects.filter(user=request.user,course=course)
        if not user_courses:
            user_course=UserCourse(user=request.user,course=course)
            user_course.save()
            course.student_num += 1
            course.save()

        user_course_pairs= UserCourse.objects.filter(course=course)
        user_id_list= [user_course.user.id for user_course in user_course_pairs]
        all_user_courses =UserCourse.objects.filter(user_id__in=user_id_list)
        course_id_list = [user_course.course.id for user_course in all_user_courses]
        related_courses=Course.objects.filter(id__in=course_id_list).order_by("click_num")[0:5]
        resources= CourseResource.objects.filter(course_id=course_id)
        return render(request, 'course-info.html', {
            'course': course,
            'related_courses':related_courses,
            'resources':resources,
        })

class CourseCommentView(LoginRequiredMixin,View):
    def get(self, request, course_id):
        course=Course.objects.get(id=course_id)
        resources = CourseResource.objects.filter(course_id=course_id)
        all_comments = course.coursecomment_set.all()
        return render(request, 'course-comment.html', {
            'course': course,
            'all_comments':all_comments,
            'resources': resources,
        })

class AddCommentView(LoginRequiredMixin,View):
    def post(self,request):
        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail","msg":"Not logged in"}', content_type='application/json')

        course_id=request.POST.get('course_id','0')
        comment =request.POST.get('comment','')

        if int(course_id)>0 and comment:
            course_comment= CourseComment()
            course= Course.objects.get(id=int(course_id))
            course_comment.course= course
            course_comment.user = request.user
            course_comment.comment= comment
            course_comment.save()
            return HttpResponse('{"status":"success","msg":"Commented Successfully"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"Comment failed"}', content_type='application/json')

class PlayVideoView(View):
    def get(self, request, video_id):
        video=Video.objects.get(id=int(video_id))
        course= video.lesson.course

        #check if user is already connected this course
        user_courses=UserCourse.objects.filter(user=request.user,course=course)
        if not user_courses:
            user_course=UserCourse(user=request.user,course=course)
            user_course.save()

        user_course_pairs= UserCourse.objects.filter(course=course)
        user_id_list= [user_course.user.id for user_course in user_course_pairs]
        all_user_courses =UserCourse.objects.filter(user_id__in=user_id_list)
        course_id_list = [user_course.course.id for user_course in all_user_courses]
        related_courses=Course.objects.filter(id__in=course_id_list).order_by("click_num")[0:5]
        resources= CourseResource.objects.filter(course=course)
        return render(request, 'course-play.html', {
            'video':video,
            'course': course,
            'related_courses':related_courses,
            'resources':resources,
        })
