from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request): 
  return HttpResponse('HOME AFONSO')


def contato(request): 
  return HttpResponse('CONTATO de Afonso Miqueias')

def sobre(request): 
  return HttpResponse('SOBRE O RECIPES')
