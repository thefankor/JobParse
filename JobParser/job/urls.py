from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('avito/vacancy/', views.search_vacancy, name='search_vacancy'),
    path('avito/resume/', views.search_resume, name='search_resume'),
    path('vacancy/', views.search_vacancy_hh, name='search_vacancy_hh'),
    path('resume/', views.search_resume_hh, name='search_resume_hh'),
    path('avito/', views.index_avito, name='home2')

]