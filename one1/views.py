from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Avengers(request):
    return HttpResponse("<h1>1)IRON MAN, 2) MR MARVEL, 3)HULK BABY, 4)NATASHA, 5)CAPTAIN</h1>")

def Hulk(request):
    return HttpResponse("<h1><marquee>GREEN BOY</marquee></h1>")
