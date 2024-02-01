from django.shortcuts import render, HttpResponse
from django.views import View
from . import views

# Create your views here.
class  IndexPageView(View):
    def get(self, reguest):
        return HttpResponse('<h1>Hello world</h1>')

