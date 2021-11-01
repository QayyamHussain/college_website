from django.urls import path
from . import views

urlpatterns = [
	path('teacher_list/', views.teacher_list, name='teacher_list'),
	path('get_teacher_skills/<str:pk>/', views.get_teacher_skills, name='get_teacher_skills')
]
