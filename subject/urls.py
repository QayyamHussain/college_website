from django.urls import path
from . import views
urlpatterns = [
	path('add_subject/', views.add_subject, name='add_subject')
]