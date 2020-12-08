from django.urls import path
from App_Login import views

app_name = 'App_Login'

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('instructor_login/', views.instructor_login, name='instructor_login'),
    path('learner_login/', views.learner_login, name='learner_login'),
    path('instructor_signup/', views.instructor_signup, name='instructor_signup'),
    path('learner_signup/', views.learner_signup, name='learner_signup'),
    path('logout/', views.logout_user, name='logout'),
    path('instructor_profile/', views.instructor_profile, name='instructor_profile'),
    path('learner_profile/', views.learner_profile, name='learner_profile'),
    path('edit_instructor/', views.edit_instructor, name='edit_instructor'),
    path('edit_learner/', views.edit_learner, name='edit_learner'),
]