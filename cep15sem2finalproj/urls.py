"""cep15sem2finalproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))

"""
from django.conf.urls import include, url
from django.contrib import admin
import acc.urls
from cep15sem2finalproj.common.views import TemplateView
from django.conf.urls.static import static
from django.conf import settings


class HomeView(TemplateView):
    template_name = "homepage.html"
    
class LoginView(TemplateView):
    template_name = "loginpage.html"
    
class EventView(TemplateView):
    template_name = "eventpage.html"
    
class RankingView(TemplateView):
    template_name = "rankinglist.html"
    
class ProfileView(TemplateView):
    template_name = "profilepage.html"

urlpatterns = [

    # subdomains
    url(r'^admin/', include(admin.site.urls)),
    url(r'^acc/', include(acc.urls.urlpatterns)),
    # page
    url(r'^home/', HomeView.as_view()),
    url(r'^login/', LoginView.as_view()),
    url(r'^event/', EventView.as_view()),
    url(r'^ranking/', RankingView.as_view()),
    url(r'^profile/', ProfileView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
