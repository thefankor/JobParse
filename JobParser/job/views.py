from django.shortcuts import render
from .parse import get_jobs, get_resumes, get_jobs_hh, get_resumes_hh
from .models import Vacancy, Resume, HHVacancy, HHResume


# Create your views here.

def index(request):
    return render(request, 'home.html', context={'type': 'hh'})

def index_avito(request):
    return render(request, 'home.html', context={'type': 'avito'})


def search_vacancy(request):
    search_query = request.GET.get('q')
    search_type = request.GET.get('new')
    print(search_query)

    code = 0
    old = True
    inf = []
    olds = Vacancy.objects.filter(title__iregex=search_query)
    if len(olds) == 0 or search_type == '1':


        vacs, code = get_jobs(search_query)

        v = Vacancy.objects.filter(title__iregex=search_query)
        v.update(is_active=False)
        for vac in vacs:
            current = Vacancy.objects.filter(out_id=vac['id'])
            if len(current) == 0:
                Vacancy.objects.create(out_id=vac['id'], href=vac['href'], title=vac['title'], desc=vac['desc'],
                                       loc=vac['loc'], price=vac['price'])
            else:
                current.update(href=vac['href'], title=vac['title'], desc=vac['desc'],
                                       loc=vac['loc'], price=vac['price'], is_active=True)

            inf = Vacancy.objects.filter(title__iregex=search_query, is_active=True)
            old = False

    else:
        inf = olds
        old = True

    return render(request, 'indexAv.html', context={'test': search_query, 'inf': inf, 'old': old, 'type':'vac', 'code': code,
                                                    'site': 'Avito'})





def search_resume(request):
    search_query = request.GET.get('q')
    search_type = request.GET.get('new')
    print(search_query)

    code = 0
    old = True
    inf = []
    olds = Resume.objects.filter(title__iregex=search_query)
    if len(olds) == 0 or search_type == '1':
        old = False
        resumes, code = get_resumes(search_query)

        r = Resume.objects.filter(title__iregex=search_query)
        r.update(is_active=False)
        for res in resumes:
            current = Resume.objects.filter(out_id=res['id'])
            if len(current) == 0:
                Resume.objects.create(out_id=res['id'], href=res['href'], title=res['title'], desc=res['desc'],
                                       bio=res['bio'], price=res['price'])
            else:
                current.update(href=res['href'], title=res['title'], desc=res['desc'],
                               bio=res['bio'], price=res['price'], is_active=True)

            inf = Resume.objects.filter(title__iregex=search_query, is_active=True)


    else:
        inf = olds
        old = True

    # for vac in slov:
    return render(request, 'indexAv.html', context={'test': search_query, 'inf': inf, 'old': old, 'type': 'res',
                                                    'code': code, 'site': 'Avito'})


def search_vacancy_hh(request):
    search_query = request.GET.get('q')
    search_type = request.GET.get('new')
    print(search_query)

    code = 0
    old = True
    inf = []
    olds = HHVacancy.objects.filter(title__iregex=search_query)
    if len(olds) == 0 or search_type == '1':

        spis = []

        vacs, code = get_jobs_hh(search_query)

        v = HHVacancy.objects.filter(title__iregex=search_query)
        v.update(is_active=False)
        for vac in vacs:
            current = HHVacancy.objects.filter(out_id=vac['id'])
            if len(current) == 0:
                a = HHVacancy.objects.create(out_id=vac['id'], href=vac['href'], title=vac['title'], area=vac['area'],
                                       salary_from=vac['salary_from'], salary_to=vac['salary_to'],
                                             metro=vac['metro'], req=vac['req'], resp=vac['resp'])
                spis.append(a)
            else:
                current.update(href=vac['href'], title=vac['title'], area=vac['area'],
                                       salary_from=vac['salary_from'], salary_to=vac['salary_to'],
                                             metro=vac['metro'], req=vac['req'], resp=vac['resp'], is_active=True)
                spis.append(current[0])

            # inf = Vacancy.objects.filter(title__iregex=search_query, is_active=True)
            inf = spis
            old = False

    else:
        inf = olds
        old = True

    return render(request, 'index2.html', context={'test': search_query, 'inf': inf, 'old': old, 'type':'vac', 'code': code,
                                                   'site': 'HH.ru'})


def search_resume_hh(request):
    search_query = request.GET.get('q')
    search_type = request.GET.get('new')
    print(search_query)

    spis = []
    code = 0
    old = True
    inf = []
    olds = HHResume.objects.filter(title__iregex=search_query)
    if len(olds) == 0 or search_type == '1':
        old = False
        resumes, code = get_resumes_hh(search_query)

        r = HHResume.objects.filter(title__iregex=search_query)
        r.update(is_active=False)
        for res in resumes:
            current = HHResume.objects.filter(out_id=res['id'])
            if len(current) == 0:
                re = HHResume.objects.create(out_id=res['id'], href=res['href'], title=res['title'], exp=res['exp'],
                                       last=res['last'], price=res['price'])
                spis.append(re)
            else:
                current.update(href=res['href'], title=res['title'], exp=res['exp'],
                                       last=res['last'], price=res['price'], is_active=True)
                spis.append(current[0])

            # inf = HHResume.objects.filter(title__iregex=search_query, is_active=True)
            inf = spis

    else:
        inf = olds
        old = True

    # for vac in slov:
    return render(request, 'index2.html', context={'test': search_query, 'inf': inf, 'old': old, 'type': 'res', 'code': code, 'site': 'HH.ru'})
