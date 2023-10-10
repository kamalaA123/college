from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'button.html')
        else:
            messages.info(request,"Invalid details")
            return redirect('Login_app:login')
    return render(request,'Login.html')
def register(request):
    if request.method=='POST':
        uname=request.POST['user']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username already exists")
                return redirect('Login_app:register')
            else:
                details=User.objects.create_user(username=uname,password=password)
                details.save()
                return render(request,'Login.html')

        else:
            messages.info(request,"Password not matching")
            return redirect('Login_app:register')
    # return redirect('/')
    return render(request,'Register.html')

def form(request):
    return render(request,'form.html')

def logout(request):
    auth.logout(request)
    return render(request,'Home.html')