from django.contrib import messages, auth
from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    # obj=place.objects.all()
    # obj1=person.objects.all()
    return render(request,"Home.html")

