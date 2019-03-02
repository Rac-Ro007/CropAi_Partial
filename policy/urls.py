# from django.urls import path
# from djan
# from .views import HomePageView,RainfallPageView

# urlpatterns = [
# 	path('',views.index),
# 	path('',HomePageView.as_view,name='home')
# 	path('rainfall/',RainfallPageView.as_view,name='rainfall')
# ]

from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^index', views.ind,name='ind'),
	url(r'^$', views.policy,name='policy'),
]