from django.shortcuts import render

# Create your views here.
from cep15sem2finalproj.common import views


class HomeView(views.TemplateView):
    template_name = "homepage.html"
