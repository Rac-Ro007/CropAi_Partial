from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$', views.home,name='home'),
	url(r'^contact/', views.contact,name='contact'),
    # path('', views.home, name='home'),
]
