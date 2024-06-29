from django.contrib import admin
from .models import Resume, Vacancy, HHResume, HHVacancy


# Register your models here.



@admin.register(Resume)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active')
    # search_fields = ['title', 'prodcategory__name']

@admin.register(Vacancy)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active')

@admin.register(HHVacancy)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary_from', 'salary_to', 'metro', 'is_active')


@admin.register(HHResume)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active')
    # search_fields = ['title', 'prodcategory__name']