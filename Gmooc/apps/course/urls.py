from django.urls import path
from .views import CourseListView, CourseDetailView, CourseInfoView, CourseCommentView, AddCommentView, PlayVideoView

#app_name='organization'
urlpatterns = [
    path('', CourseListView.as_view(), name="course-list"),
    path('detail/<course_id>/', CourseDetailView.as_view(), name="course-detail" ),
    path('info/<course_id>/', CourseInfoView.as_view(), name="course-info" ),
    path('comment/<course_id>/', CourseCommentView.as_view(), name="course-comment" ),
    path('add_comment/', AddCommentView.as_view(), name="add_comment" ),
    path('video/<video_id>/', PlayVideoView.as_view(), name="play_video"),
]