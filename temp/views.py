from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render,HttpResponseRedirect
import requests

# Create your views here.

def temp(request):
	return render(request , 'temp.html')
	#return HttpResponse('<h1>Hey I have Done it</h1>')
def ind(request):
	return render(request , 'index.html')
# class HomePageView(TemplateView):