from django.conf.urls import include, url
from . import views

urlpatterns = [
		# url(r'^$', 'signups.signups.home' ,name= 'home') 
		url(r'^$', views.signup2),
		# url(r'^(?P<id>\d+)/$', views.signup),
		]
    
