from django.urls import path,re_path
from apps.course.views import CourseListView

# 要写上app的名字
app_name = "course"

urlpatterns = [
    path('list/',CourseListView.as_view(),name='course_list'),

]