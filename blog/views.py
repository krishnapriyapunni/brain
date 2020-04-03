from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import User
from django.conf import settings
from django.views import generic
# from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
# import pandas
# import pandas as pd
# import seaborn as sns
# from pandas.plotting import scatter_matrix
# import matplotlib.pyplot as plt
# from sklearn import model_selection
# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import accuracy_score
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from sklearn.naive_bayes import GaussianNB
# import os

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Document
from .forms import UploadFileForm

def index(request):
	return render(request,'index.html',{})
def contact(request):
	return render(request,'contact.html',{})
def about(request):
	return render(request,'about.html',{})



def signout(request):
	logout(request)
	return HttpResponseRedirect('/')

def log_in(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(username=email,password=password)
		if user:
			print (user)
			login(request,user)
			return HttpResponseRedirect(reverse('about'))
			# return render(request,'about.html', {"msg3":'Login Successfully'})
		else:
			# error="sorry"
			return render(request,'index.html',{"msg2":'UNABLE TO LOGIN '})
	else:
		return render(request,'index.html',{})
	# else:
	#   return render(request,'login.html',{})  
	return render(request,'index.html',{})


def signup(request):
	if request.method=='POST':
		name = request.POST.get('name')
		mobile = request.POST.get('mobile')
		password = request.POST.get('password')
		email = request.POST.get('email')

		user1=UserProfile.objects.filter(email=email,password=password).exists()
		if not user1:   
			user2=User.objects.create_user(
				username=email,
				password=password,
				)
			
			user_pro=UserProfile.objects.create(
				user=user2,
				email=email,
				password=password,
				mobile=mobile,
				
			)
			user_pro.save()
			return render(request,'index.html',{"msg1":'you are logined'})
		else:
			error='you r already signed'
			return render(request,'index.html',{'error':error})


		# return render(request,'login.html',{"msg1":'you are logined'})
	else:
		return render(request,'index.html',{})
	return render(request,'index.html',{})

 
def result(request):
	
	return render(request, 'result.html')
def simple_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ModelWithFileField(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('index')
    else:
        form = UploadFileForm()
    return render(request, 'prediction.html', {'form': form})
def prediction1(request):
	return render(request, 'prediction1.html')

def prediction(request):

	path = ('/media/atees/DATA/maneesha/alzheimersnew/mysite/blog/')
	files = os.listdir(path)
	for file in files:
		if file.endswith('.csv'):
			dataset = pd.read_csv(path+file)
			# Load dataset
			print(dataset.shape)

# head
			
			return render(request,'result.html',{})     
			