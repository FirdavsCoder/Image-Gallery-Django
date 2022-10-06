from django.shortcuts import render

from .models import Picture
# Create your views here.


def home(request):
    post = Picture.objects.all()
    return render(request,'index.html',{"posts":post})
