from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from myapp import forms
# Create your views here.

@login_required
def profile(request):
    print(dir(request.user))
    context = {
    'username': request.user,
    'first_name': request.user.first_name,
    'email': request.user.email,
    'last_login': request.user.last_login,
    'date_joined': request.user.date_joined,
    }
    return render(request, 'profile.html', context)

def welcome(request):
    return render(request,'welcome.html')

def SignUP(request):
    form = forms.myform()
    if request.method == 'POST':
        form = forms.myform(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/signin')
        else:
            print(form.errors)
    return render(request,'registeration.html',{'form':form})

def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/signin')

def Sign_in(request):
    if request.method == "POST":
        name = request.POST['un']
        pswd = request.POST['pwd']
        user = authenticate(username=name, password=pswd)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/profile')
        else:
            wrngpass=("Sorry!! You are not authenticated!!! please check your User Name And Password")
            return render(request,'login.html',{'wrngpass':wrngpass})
    return render(request,'login.html')
