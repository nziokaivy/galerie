from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image,Category,Location
# Create your views here.

def index(request):
    new_image = Image.get_image()
    return render(request,'index.html',{"new_image":new_image})