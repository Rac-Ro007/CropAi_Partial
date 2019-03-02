from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render,HttpResponseRedirect
import requests

# Create your views here.

def rainfall(request):
	return render(request , 'rainfall.html')
	#return HttpResponse('<h1>Hey I have Done it</h1>')
def ind(request):
	return render(request , 'index.html')
# class HomePageView(TemplateView):
# 	template_view = "index.html"

# class RainfallPageView(TemplateView):
# 	template_view = "rainfall.html"