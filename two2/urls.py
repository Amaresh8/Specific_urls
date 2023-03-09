from two2.views import *
from django.urls import path
app_name="Thor"
urlpatterns = [
    path("Thor/",Thor,name="Thor"),
]