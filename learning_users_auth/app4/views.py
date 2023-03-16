from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from app4.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse 
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'app4/index.html')

@login_required
def special(request):
    return HttpResponse('You are logged in')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registerted = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)

            user.save()

            userprofile = profile_form.save(commit=False)
            userprofile.user = user


            if 'profile_pic' in request.FILES:
                userprofile.profile_pic = request.FILES['profile_pic']
            
            userprofile.save()
            
            registerted=True
        else:
          print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'app4/register.html',{'user_form':user_form,
                                                'profile_form':profile_form,
                                                'registered':registerted
                                                })

def user_login(request):

    if request.method=="POST":
        username = request.POST.get('username') 
        password = request.POST.get('password')  

        user=authenticate(username=username,password=password) 

        if user:
            if user.is_active:
                 login(request,user)
                 return HttpResponseRedirect(reverse('index'))  
            else:
                return HttpResponse("Account not activated") 
        else:
            print("username:{} and Pasword: {}".format(username,password)) 
            return HttpResponse("invalid request") 
    else:
        return render(request,'app4/login.html',{})                                                           