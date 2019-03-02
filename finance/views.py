from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render,HttpResponseRedirect
import requests

# Create your views here.

def finance(request):
	return render(request , 'finance.html')

def finance_exp(request):
	return render(request , 'finance_exp.html')

def finance_tb(request):
	return render(request , 'finance_tb.html')

def emi_cal(request):
	return render(request , 'emi_cal.html')
	#return HttpResponse('<h1>Hey I have Done it</h1>')
def ind(request):
	return render(request , 'index.html')
# class HomePageView(TemplateView):