from statistics import mean

from django.db.models import Avg, Value, Case, When, IntegerField
from django.db.models.functions import Coalesce
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
            print(res)
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
    sort = request.GET.get('sort')
    exp = request.GET.get('exp')
    emp = request.GET.get('emp')
    print(search_query)

    salary_avg = 0
    salary = []
    code = 0
    old = True
    inf = []
    olds = HHVacancy.objects.filter(title__iregex=search_query).filter(is_active=True)

    if (exp != 'None' and exp) and (emp != 'None' and emp):
        olds = olds.filter(experience=exp, employment=emp)
        print('a')
    elif exp != 'None' and exp and (emp == None or emp == 'None'):
        olds = olds.filter(experience=exp)
        print('b')
    elif emp != 'None' and emp and (exp == None or exp == 'None'):
        olds = olds.filter(employment=emp)
        print('c')

    if len(olds) == 0 or search_type == '1':
        # print('new')

        spis = []
        ids = []

        vacs, code = get_jobs_hh(search_query, exp, emp)

        v = HHVacancy.objects.filter(title__iregex=search_query)
        v.update(is_active=False)
        for vac in vacs:
            current = HHVacancy.objects.filter(out_id=vac['id'])
            if len(current) == 0:
                a = HHVacancy.objects.create(out_id=vac['id'], href=vac['href'], title=vac['title'], area=vac['area'],
                                       salary_from=vac['salary_from'], salary_to=vac['salary_to'],
                                             metro=vac['metro'], req=vac['req'], resp=vac['resp'],
                                             experience = vac['experience'], employment = vac['employment'])
                spis.append(a)
                ids.append(a.pk)

            else:
                current.update(href=vac['href'], title=vac['title'], area=vac['area'],
                                       salary_from=vac['salary_from'], salary_to=vac['salary_to'],
                                             metro=vac['metro'], req=vac['req'], resp=vac['resp'],
                                             experience = vac['experience'], employment = vac['employment'], is_active=True)
                spis.append(current[0])
                ids.append(current[0].pk)
            if vac['salary_from'] and vac['salary_to']:
                salary.append((int(vac['salary_from']) + int(vac['salary_to']))/2)
            elif vac['salary_from']:
                salary.append(int(vac['salary_from']))
            elif vac['salary_to']:
                salary.append(int(vac['salary_to']))

            # inf = Vacancy.objects.filter(title__iregex=search_query, is_active=True)
            if len(salary)>0:
                salary_avg = int(mean(salary))
            else:
                salary_avg = None

            if sort == '1':
                inf = HHVacancy.objects.filter(pk__in=ids)
                inf =  inf.annotate(
                nulls_last=Case(
                    When(salary_from__isnull=True, then=Value(1)),
                    When(salary_from__isnull=False, then=Value(0)),
                    output_field=IntegerField(),
                )
            ).order_by('nulls_last', '-salary_from')
            else:
                inf = spis
            old = False


    else:
        average_salary_from = olds.exclude(salary_from__isnull=True).aggregate(Avg('salary_from'))['salary_from__avg']
        average_salary_to = olds.exclude(salary_from__isnull=True).aggregate(Avg('salary_to'))['salary_to__avg']
        salary_avg = int((average_salary_to or 0 + average_salary_from or 0)/2)
        # inf = olds
        old = True
        # print('old')



        if sort == '1':
            # inf = olds.order_by('-salary_from')
            # inf = olds.annotate(
            #         sort_salary=Coalesce('salary_from', '0')
            #     ).order_by('-salary_from')


            inf = olds.annotate(
                nulls_last=Case(
                    When(salary_from__isnull=True, then=Value(1)),
                    When(salary_from__isnull=False, then=Value(0)),
                    output_field=IntegerField(),
                )
            ).order_by('nulls_last', '-salary_from')
        else:

            inf = olds

    return render(request, 'index2.html', context={'test': search_query, 'inf': inf, 'old': old, 'type':'vac', 'code': code,
                                                   'site': 'HH.ru', 'avg': salary_avg, 'sort': sort or '0',
                                                   'employment': emp or 'None', 'experience': exp or 'None'})


def search_resume_hh(request):
    search_query = request.GET.get('q')
    sort = request.GET.get('sort')
    search_type = request.GET.get('new')
    print(search_query)

    ids = []
    salary = []
    salary_avg = 0
    spis = []
    code = 0
    old = True
    inf = []
    olds = HHResume.objects.filter(title__iregex=search_query)
    if len(olds) == 0 or search_type == '1':
        print('new')
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
                ids.append(re.pk)
            else:
                current.update(href=res['href'], title=res['title'], exp=res['exp'],
                                       last=res['last'], price=res['price'], is_active=True)
                spis.append(current[0])
                ids.append(current[0].pk)

            if res['price']:
                salary.append(int(res['price']))
        try:
            salary_avg = int(mean(salary))
        except:
            salary_avg = None

        # inf = HHResume.objects.filter(title__iregex=search_query, is_active=True)
        # inf = spis
        if sort == '1':
            inf = HHResume.objects.annotate(
                nulls_last=Case(
                    When(price__isnull=True, then=Value(1)),
                    When(price__isnull=False, then=Value(0)),
                    output_field=IntegerField(),
                )
            ).order_by('nulls_last', '-price')
        else:
            inf = spis
    else:
        print('old')
        salary_avg = int(olds.exclude(price__isnull=True).aggregate(Avg('price'))['price__avg'])
        if sort == '1':
            inf = olds.annotate(
                nulls_last=Case(
                    When(price__isnull=True, then=Value(1)),
                    When(price__isnull=False, then=Value(0)),
                    output_field=IntegerField(),
                )
            ).order_by('nulls_last', '-price')
        else:
            inf = olds
        old = True

    # for vac in slov:
    return render(request, 'index2.html', context={'test': search_query, 'inf': inf, 'old': old, 'type': 'res',
                                                   'code': code, 'site': 'HH.ru', 'avg': salary_avg, 'sort': sort or '0'})
