from django.shortcuts import render
# django import
from django.views.generic import TemplateView

# Create your views here.

class LoginUserView(TemplateView):
    template_name = "users/login.html"

