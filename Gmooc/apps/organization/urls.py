from django.urls import path
from .views import OrgView, UserConsultView, OrgHomeView, OrgCourseView, OrgInstrView, OrgDescView

#app_name='organization'
urlpatterns = [
    path('',OrgView.as_view(), name="org_list"),
    path('user_consult/',UserConsultView.as_view(), name="user_consult"),
    path('home/<org_id>/',OrgHomeView.as_view(), name="org_home"),
    path('courses/<org_id>/', OrgCourseView.as_view(), name="org_course"),
    path('instructors/<org_id>/', OrgInstrView.as_view(), name="org_instr"),
    path('description/<org_id>/', OrgDescView.as_view(), name="org_desc"),
]