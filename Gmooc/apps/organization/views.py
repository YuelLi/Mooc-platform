from django.shortcuts import render,render_to_response
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg
from .models import CityDict
# Create your views here.


class OrgView(View):
    def get(self,request):
        all_orgs= CourseOrg.objects.all()
        org_num=all_orgs.count()
        all_cities= CityDict.objects.all()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        org_paginator = Paginator(all_orgs, 3, request=request)
        orgs = org_paginator.page(page)

        return render_to_response('org-list.html', {
            'all_orgs': orgs,
            'org_num':org_num,
            'all_cities':all_cities
        })


