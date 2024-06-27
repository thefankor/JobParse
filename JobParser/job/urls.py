from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('vacancy/', views.search_vacancy, name='search_vacancy'),
    path('resume/', views.search_resume, name='search_vresume'),
]