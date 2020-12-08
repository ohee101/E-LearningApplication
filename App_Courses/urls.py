from django.urls import path
from App_Courses import views

app_name = 'App_Courses'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('publish/', views.PublishCourse.as_view(), name='publish'),
    path('course_description/', views.course_description, name='course_description'),
    path('my_courses/', views.MyCourses.as_view(), name='my_courses'),
    path('question/<pk>/', views.question, name='question'),
]
