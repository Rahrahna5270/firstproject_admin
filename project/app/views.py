from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from.models import *


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('dash')
            else:
                messages.error(request, 'You are not a superuser!')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'home.html')

def dashboard(request):
    admins=Admin.objects.all()
    return render(request,'dashboard.html',{'admins':admins})
def create(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        admins=Admin.objects.create(name=name,email=email,phone=phone,username=username,password=password)
        admins.save()
        print(admins)
        return redirect('dash')
    return render(request,'create.html')
def viewadmin(request,id):
    admins=Admin.objects.get(id=id)
    return render(request,'viewadmin.html',{'admins':admins})
def delete(request,id):
    admins=Admin.objects.get(id=id)
    admins.delete()
    return redirect('dash')
def edit(request,id):
    edit=Admin.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        if edit:
            edit.name=name
            edit.email=email
            edit.phone=phone
            edit.username=username 
            edit.password=password
            edit.save()
        return redirect('dash')
    return render (request,'edit.html')
def user_logout(request):
    logout(request)
    return redirect('home')