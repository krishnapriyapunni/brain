from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('',views.index,name='index'),
	path('signup/',views.signup,name='signup'),
	path('login/',views.log_in,name='login'),
	path('about/',views.about,name='about'),
	path('prediction',views.prediction,name='prediction'),
	path('contact/',views.contact,name='contact'),
	# path('gallery/',views.gallery,name='gallery'),
	path('uploads/simple/',views.simple_upload, name='simple_upload'),
	# path('uploads/simple/',views.simple_upload, name='simple_upload'),

	path('result/',views.result, name='result'),
	path('prediction1/',views.prediction1, name='prediction1'),
]
#  url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
