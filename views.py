from django.shortcuts import render
from django.template import loader
from .models import RegisterModel
from .forms import RegisterForm

def home_view(request):
    context = {}
    form = RegisterForm(request.POST or None, request.FILES or None)    
    if form.is_valid():
        form.save()
    context['form']= form
    return  render(request,"hello.html",context) 
