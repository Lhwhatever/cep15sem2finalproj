from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url('login', views.LoginView.as_view()),
)
