from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['body'] = 'Thank you!'
    context['title'] = 'OK!'
    return render(request, 'hello.html', context)
