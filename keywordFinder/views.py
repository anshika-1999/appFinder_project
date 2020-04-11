import requests
import json
import validators
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
from . import models

def keyword(request):
    return render(request, 'keywordFinder/keyword.html' )

def urlkeyword(request):
    if request.method == 'GET':
        v=0
        url = request.GET['url']
        if url=='':
            v=2
            params = {
                'v':v
            }
            return HttpResponse(json.dumps(params),content_type="application/json")
        valid=validators.url(url)
        print(valid)
        if valid!=True:
            v=1
            params = {
                'v':v
            }
            return HttpResponse(json.dumps(params),content_type="application/json")
        elif valid==True:
            c=models.Url_Keyword.objects.filter(url=url).count()
            if c>=1:
                flag=True
            else:
                flag=False
                b=models.Url_Keyword.objects.create(url=url,keywords='')
            if flag==False:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, features='html.parser')
                meta = soup.find_all('meta',{'name':'keywords'})
                lst=[]
                for tags in meta:
                    lst.append(tags['content'])
                key=[]
                temp=[]
                rec=[]
                for item in lst:
                    temp=item.split(',')
                    for t in temp:
                        key.append(t.lower().strip())
                for k in key:
                    if b.keywords=='':
                        b.keywords=k
                    else:
                        b.keywords=b.keywords+'+'
                        b.keywords=b.keywords+k
                b.save()
                all_entries = models.Url_Keyword.objects.all()
                for entries in all_entries:
                    if entries.url!=url:
                        words=entries.keywords
                        words=words.split('+')
                        c=0
                        for k in key:
                            for word in words:
                                if k==word:
                                    c+=1
                                    break
                        if c>=3:
                            for word in words:
                                if word not in key:
                                    rec.append(word)
            if flag==True:
                    rec=[]
                    key_url = models.Url_Keyword.objects.get(url=url)
                    key = key_url.keywords
                    key = key.split('+')
                    all_entries = models.Url_Keyword.objects.all()
                    for entries in all_entries:
                        if entries.url!=url:
                            words=entries.keywords
                            words=words.split('+')
                            c=0
                            for k in key:
                                if k in words:
                                    c+=1
                            if c>=3:
                                for word in words:
                                    if word not in key:
                                        rec.append(word)
            params = {
                'keywords':key,
                'reckeywords':rec,
                'v':v
            }
            return HttpResponse(json.dumps(params),content_type="application/json")
