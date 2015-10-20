from django.shortcuts import render

# Create your views here.
from cep15sem2finalproj import common


class EventView(common.views.ListView):
    template_name = "eventpage.html"


class RankingView(common.views.ListView):
    template_name = "rankinglist.html"
