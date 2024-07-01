import time

import requests
from bs4 import BeautifulSoup as BS
def get_jobs(title):
    UserAgent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Acoo Browser; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 2.0.50727)'
    host = 'https://www.avito.ru/'


    cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'
    headers = {
        'content-type': "application/json;charset=utf-8",
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.684 Yowser/2.5 Safari/537.36',
    }

    if cookie:
        headers['cookie'] = cookie

    vakansii = []
    a = []

    for i in range(1, 2):
        url = f'https://www.avito.ru/moskva/vakansii?cd=1&p={str(i)}&q={title}&s=104'
        # url = 'https://chipi-chipi.ru'
        # url = 'https://www.avito.ru/'
        r = requests.get(url, headers=headers, timeout=15)
        # time.sleep(10)


        print(r.status_code)
        # if r.status_code == 403:
        #     print(r.text)
        # f = open('avvvv.html', 'w')
        # f.write(r.text)
        # f.close()

        soup = BS(r.text, "html.parser")

        vak = soup.findAll('div', class_='iva-item-vacancy-_fQrr')
        if len(vak) == 0:
            break
        # print(vak)

        for v in vak:
            info = dict()
            if v.find('a', 'styles-module-root-iSkj3'):
                title = v.find('a', 'styles-module-root-iSkj3')
                info['title'] = title.text.replace('\xa0', ' ').replace('\x00', '')
            else:
                continue

            info['id'] = int(v.get('data-item-id'))
            info['href'] = title.get('href')

            if v.find('div', class_='price-price-JP7qe'):
                price = v.find('div', class_='price-price-JP7qe').text
                price = price.replace('\xa0', '').replace('\x00', '')
                info['price'] = price
            else:
                info['price'] = None

            if v.find('div', class_='iva-item-descriptionStep-C0ty1'):
                desc = v.find('div', class_='iva-item-descriptionStep-C0ty1').text.replace('\xa0', ' ').replace('\x00', '')
                # desc = desc.replace('\xa0', ' ')
                # desc = desc.replace('\n', '<br>')
                info['desc'] = desc
            else:
                info['desc'] = None

            if v.find('div', class_='geo-root-zPwRk'):
                loc = v.find('div', class_='geo-root-zPwRk')
                info['loc'] = loc.text.replace('\xa0', ' ').replace('\x00', '')
                # print(loc.text)
            else:
                info['loc'] = None

            vakansii.append(info)

    # print(vakansii)
    print(len(vakansii))
    return vakansii, r.status_code

# get_jobs('программист')

def get_resumes(title):
    UserAgent = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Acoo Browser; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 2.0.50727)'
    host = 'https://www.avito.ru/'


    cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'
    headers = {
        'content-type': "application/json;charset=utf-8",
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.684 Yowser/2.5 Safari/537.36',
    }

    if cookie:
        headers['cookie'] = cookie

    vakansii = []
    a = []

    for i in range(1, 2):
        url = f'https://www.avito.ru/moskva/rezume?cd=1&p={str(i)}&q={title}&s=104'
        r = requests.get(url, headers=headers, timeout=15)
        print(r.status_code)
        # if r.status_code == 403:
        #     print(r.text)
        # f = open('avvvv.html', 'w')
        # f.write(r.text)
        # f.close()

        soup = BS(r.text, "html.parser")

        vak = soup.findAll('div', class_='iva-item-root-_lk9K')
        if len(vak) == 0:
            break
        # print(vak)

        for v in vak:
            info = dict()
            if v.find('a', 'styles-module-root-iSkj3'):
                title = v.find('a', 'styles-module-root-iSkj3')

                info['title'] = title.text.replace('\x00', '')
                info['href'] = title.get('href')
            else:
                continue

            info['id'] = int(v.get('data-item-id'))

            if v.find('div', class_='price-price-JP7qe'):
                price = v.find('div', class_='price-price-JP7qe').text
                price = price.replace('\xa0', '')
                info['price'] = price
            else:
                info['price'] = None

            if v.find('div', class_='iva-item-descriptionStep-C0ty1'):
                desc = v.find('div', class_='iva-item-descriptionStep-C0ty1').text
                desc = desc.replace('\xa0', ' ').replace('\x00', '')
                info['desc'] = desc
            else:
                info['desc'] = None

            if v.find('span', class_='iva-item-text-Ge6dR'):
                bio = v.find('span', class_='iva-item-text-Ge6dR')
                info['bio'] = bio.text.replace('\xa0', ' ').replace('\x00', '')
                # print(loc.text)
            else:
                info['bio'] = None


            vakansii.append(info)

    # print(vakansii)
    print(len(vakansii))
    return vakansii, r.status_code


def get_jobs_hh(title, exp='None', emp='None'):
    import requests
    import json

    headers = {
        'content-type': "application/json;charset=utf-8",
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.684 Yowser/2.5 Safari/537.36',
    }

    vakansii = []

    url = (f'https://api.hh.ru/vacancies?text={title}&per_page=50&area=1')
    if exp != 'None':
        url = url +f'&experience={exp}'
    if emp != 'None':
        url = url +f'&employment={emp}'
    r = requests.get(url, headers=headers, timeout=15)

    print(r.status_code)

    try:
        vacs = json.loads(r.text)['items']
    except:
        return [], r.status_code

    # print(vacs)
    for vac in vacs:
        info = dict()
        info['id'] = vac['id']
        info['title'] = vac['name']
        info['area'] = vac['area']['name']
        info['href'] = vac['alternate_url']

        # if vac['salary']
        if vac['salary']:
            info['salary_from'] = vac['salary']['from']
            info['salary_to'] = vac['salary']['to']
        else:
            info['salary_from'] = None
            info['salary_to'] = None

        info['metro'] = None
        if vac['address']:
            if vac['address']['metro']:
                if vac['address']['metro']['station_name']:
                    info['metro'] = vac['address']['metro']['station_name']

        info['experience'] = vac['experience']
        info['employment'] = vac['employment']
        if vac['experience']:
            info['experience'] = vac['experience']['id']
        if vac['employment']:
            info['employment'] = vac['employment']['id']

        info['req'] = None
        info['resp'] = None
        if vac['snippet']:
            if vac['snippet']['requirement']:
                info['req'] = vac['snippet']['requirement'].replace('</highlighttext>', '').replace('<highlighttext>', '')
            else:
                info['req'] = vac['snippet']['requirement']

            if vac['snippet']['responsibility']:
                info['resp'] = vac['snippet']['responsibility'].replace('</highlighttext>', '').replace('<highlighttext>', '')
            else:
                info['resp'] = vac['snippet']['responsibility']
        vakansii.append(info)

    return vakansii, r.status_code


def get_resumes_hh(title):
    headers = {
        'content-type': "application/json;charset=utf-8",
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.684 Yowser/2.5 Safari/537.36',
    }

    vakansii = []
    a = []

    url = f'https://hh.ru/search/resume?area=1&exp_period=all_time&logic=normal&no_magic=true&order_by=relevance&ored_clusters=true&pos=full_text&search_period=0&text={title}&items_on_page=50'
    r = requests.get(url, headers=headers, timeout=15)

    # print(r.text)
    f = open('hh.html', 'w')
    f.write(r.text)
    f.close()

    soup = BS(r.text, "html.parser")

    vak = soup.findAll('div', class_='wrapper--eiknuhp1KcZ2hosUJO7g')

    # if len(vak) == 0:
    # break

    # print(vak)

    for v in vak:
        info = dict()
        if v.find('a', 'bloko-link'):
            title = v.find('a', 'bloko-link')
            info['title'] = title.text
        else:
            continue

        info['id'] = v.get('data-resume-id')
        info['href'] = title.get('href')

        if v.find('div', class_='bloko-text bloko-text_strong'):
            price = v.find('div', class_='bloko-text bloko-text_strong').text
            price = price.replace('\u2009', '')
            price = price.replace('\xa0', '')
            price = price.replace(' ', '')
            price = price.replace('₽', '')

            try:
                info['price'] = int(price)
            except:
                continue
        else:
            info['price'] = None

        if v.find('div', class_='content--uYCSpLiTsRfIZJe2wiYy'):
            exp = v.find('div', class_='content--uYCSpLiTsRfIZJe2wiYy').text
            # price = price.replace('\u2009', ' ')
            # price = price.replace('\xa0', ' ')

            info['exp'] = exp
        else:
            info['exp'] = None

        if v.find('span', class_='bloko-text bloko-text_strong'):
            last = v.find('span', class_='bloko-text bloko-text_strong')
            info['last'] = last.text
            # print(loc.text)
        else:
            info['last'] = None

        vakansii.append(info)

    return vakansii, r.status_code
