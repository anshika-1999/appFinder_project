import requests
import json
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse

BASE_GOOGLE_URL = "https://play.google.com/store/apps/details?id={}"
BASE_APP_STORE_URL = "https://apps.apple.com/in/app/{name}/id{id}"

def home(request):
    return render(request, 'appSearch/home.html')

def search(request):
    return render(request, 'appSearch/search.html' )

def googlePlay(request):
    if request.method == 'GET':
        package = request.GET['package']
        final_url = BASE_GOOGLE_URL.format(package)
        response = requests.get(final_url)
        data = response.text
        soup = BeautifulSoup(data, features='html.parser')
        title = soup.find_all('h1', {'itemprop':'name'})
        title=title[0].find_all('span')
        title = title[0].text

        dev = soup.find_all('a', {'class': 'hrTbp R8zArc' })
        dev=dev[0].text

        desc = soup.find_all('div', {'jsname': 'sngebd'})
        desc=desc[0].text

        installs = soup.find_all('div', {'class': 'hAyfc'})
        for install in installs:
            if 'Installs' in install.text:
                i=install.text[8:]

        ratingNumber = soup.find_all('span', {'class': 'AYi5wd TBRnV'})
        ratingNumber=ratingNumber[0].text


        rating = soup.find_all('div', {'class': 'BHMmbe'})
        rating=rating[0].text

        img = soup.find_all('div', {'class': 'xSyT2c'})
        img = img[0].find('img').get('src')

        params = {
        'title':title,
        'developer':dev,
        'numReview':ratingNumber,
        'rating':rating,
        'description':desc[:201],
        'furtherdescription':desc[201:],
        'image':img,
        'installs':i,
        }
        return HttpResponse(json.dumps(params),content_type="application/json")
    else:
        return HttpResponse("Request method is not a GET")

def appStore(request):
    if request.method == 'GET':
        appname = request.GET['appname']
        appid = request.GET['appid']
        final_url = BASE_APP_STORE_URL.format(name=appname,id=appid)
        response = requests.get(final_url)
        data = response.text

        soup = BeautifulSoup(data, features='html.parser')
        title = soup.find_all('h1', {'class':'product-header__title app-header__title'})
        title = title[0].text
        title=title.split('\n')
        title=title[1].rsplit()
        title = ' '.join(title)

        dev = soup.find_all('h2', {'class': 'product-header__identity app-header__identity' })
        dev=dev[0].text
        dev=dev.rsplit()
        dev = ' '.join(dev)

        desc = soup.find_all('div', {'class': 'section__description'})
        desc=desc[0].text
        desc=desc.split('\n')[4]

        ratingNumber = soup.find_all('div', {'class': 'we-customer-ratings__count small-hide medium-show'})
        ratingNumber=ratingNumber[0].text
        ratingNumber = ratingNumber.split()[0]

        rating = soup.find_all('span', {'class': 'we-customer-ratings__averages__display'})
        rating=rating[0].text

        img = soup.find_all('picture', {'class': 'we-artwork ember-view product-hero__artwork we-artwork--fullwidth we-artwork--ios-app-icon'})
        img = img[0].find_all('img', {'class': 'we-artwork__image'})
        img = img[0].get('src')

        params = {
        'title':title,
        'developer':dev,
        'numReview':ratingNumber,
        'rating':rating,
        'description':desc[:201],
        'furtherdescription':desc[201:],
        'image':img,
        }
        return HttpResponse(json.dumps(params),content_type="application/json")
    else:
        return HttpResponse("Request method is not a GET")
