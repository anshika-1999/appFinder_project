from django.shortcuts import render

def search(request):
    return render(request, 'appSearch/search.html' )
