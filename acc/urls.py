from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

    url(r'^inbox/$', views.InboxView.as_view(), name='inbox'),
    url(r'^compose/$', views.ComposeView.as_view(), name='compose'),
)
