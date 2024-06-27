from django.shortcuts import render
from .parse import get_jobs
from .models import Vacancy
# Create your views here.

def index(request):
    return render(request, 'index.html', context={'test': 'KAUF'})

def search_vacancy(request):
    search_query = request.GET.get('q')
    print(search_query)
    slov = get_jobs(search_query)

    # for vac in slov:
    return render(request, 'index.html', context={'test': search_query, 'inf': slov})


def search_resume(request):
    search_query = request.GET.get('q')
    print(search_query)
    slov = get_jobs(search_query)

    # for vac in slov:
    return render(request, 'index.html', context={'test': search_query, 'inf': slov})