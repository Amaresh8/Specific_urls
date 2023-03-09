from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Thor(request):
    return HttpResponse("THOR(URUMALA DORA)")
