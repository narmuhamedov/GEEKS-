from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def message(request):
    return HttpResponse('Это мой первый проект на DJANGO')

def emodji(request):
    return HttpResponse('😀😄🤬🫨🙃💩')