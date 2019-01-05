from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg
from .models import CityDict
from .forms import UserConsultForm
from course.models import Course
# Create your views here.


class OrgView(View):
    def get(self,request):
        all_orgs= CourseOrg.objects.all()
        all_cities= CityDict.objects.all()

        top_orgs=all_orgs.order_by("-click_num")[:3]

        # filtered by city
        city_id=request.GET.get('city','')
        if city_id:
            all_orgs=all_orgs.filter(city_id=int(city_id))

        # filtered by category
        category= request.GET.get('ct','')
        if category:
            all_orgs=all_orgs.filter(category=category)

        # sorted by student num and click num
        sort=request.GET.get('sort','')
        if sort:
            if sort=="students":
                all_orgs=all_orgs.order_by("-student_num")
            elif sort=="courses":
                all_orgs=all_orgs.order_by("-course_num")


        org_num = all_orgs.count()

        #pagination
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        org_paginator = Paginator(all_orgs, 3, request=request)
        orgs = org_paginator.page(page)

        return render(request,'org-list.html', {
            'all_orgs': orgs,
            'all_cities':all_cities,
            'top_orgs':top_orgs,
            'org_num': org_num,
            'city_id':city_id,
            'category':category,
            'sort':sort
        })


class UserConsultView(View):
    def post(self,request):
        user_consult_form=UserConsultForm(request.POST)
        if user_consult_form.is_valid():
            user_consult= user_consult_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"add error"}', content_type='application/json')

class OrgHomeView(View):
    def get(self,request, org_id):
        course_org =CourseOrg.objects.get(id=int(org_id))
        all_courses =course_org.course_set.all()[:3]
        all_instructors= course_org.instructor_set.all()[:1]
        current_page="home"
        return render(request,'org-detail-homepage.html',{
            'course_org':course_org,
            'all_courses':all_courses,
            'all_instructors':all_instructors,
            'current_page':current_page
        })

class OrgCourseView(View):
    def get(self,request, org_id):
        course_org =CourseOrg.objects.get(id=int(org_id))
        all_courses =course_org.course_set.all()
        current_page = "courses"
        return render(request,'org-detail-course.html',{
            'course_org':course_org,
            'all_courses':all_courses,
            'current_page': current_page
        })


class OrgInstrView(View):
    def get(self,request, org_id):
        course_org =CourseOrg.objects.get(id=int(org_id))
        all_instructors= course_org.instructor_set.all()
        current_page = "instr"
        return render(request,'org-detail-instructors.html',{
            'course_org':course_org,
            'all_instructors': all_instructors,
            'current_page': current_page
        })


class OrgDescView(View):
    def get(self,request, org_id):
        course_org =CourseOrg.objects.get(id=int(org_id))
        current_page = "desc"
        return render(request,'org-detail-desc.html',{
            'course_org':course_org,
            'current_page': current_page
        })




