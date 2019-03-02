from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^index', views.ind,name='ind'),
	path('', views.finance,name='finance'),
	path('finance_tb/', views.finance_tb,name='finance_tb'),
	path('finance_exp/', views.finance_exp,name='finance_exp'),
	path('emi_cal/', views.emi_cal,name='emi_cal'),
    # path('', views.home, name='home'),
]