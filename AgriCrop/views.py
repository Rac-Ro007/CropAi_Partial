from django.shortcuts import render,HttpResponseRedirect

def index1(request):
 	return render(request,'index.html')

def rainfall(request):
	return HttpResponseRedirect('rainfall.html')

def policy(request):
	return HttpResponseRedirect('policy.html')

def temp(request):
	return HttpResponseRedirect('temp.html')

def predict_crop(request):
	return HttpResponseRedirect('predict_crop.html')