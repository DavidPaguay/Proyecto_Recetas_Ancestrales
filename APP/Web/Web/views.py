from django import template
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

def home (request):

   return render(request,"InicioS.html")