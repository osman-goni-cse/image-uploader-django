from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from .forms import ImageForm
from .models import Image
# Create your views here.

def home(request):
  form = ImageForm()
  img = Image.objects.all() 

  if request.method == "POST":
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
    else:
      print(form.errors)
      return render(request, 'my_app/home.html', {'form':form, 'img':img})
      
  
  return render(request, 'my_app/home.html', {'form':form, 'img':img})