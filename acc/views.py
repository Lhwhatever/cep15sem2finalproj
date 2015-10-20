from django.contrib import auth
from django.contrib.auth import views as authviews
from django.shortcuts import render

# Create your views here.
from django.views import generic
from cep15sem2finalproj import common
from cep15sem2finalproj.common.views import redirect_with_msg


class LoginView(common.views.FormView):

    template_name = 'loginpage.html'

    def dispatch(self, request, *args, **kwargs):
        return redirect_with_msg(request, 'You are already logged in.', 'home', permanent=False, *args, **kwargs) \
            if request.user.is_authenticated() else authviews.login(request, next_page='/')


class LogoutView(generic.View):

    def dispatch(self, request, *args, **kwargs):
        request.session['Message'] = 'Logged out successfully.' if request.user.is_authenticated() else None

        return authviews.logout(request, next_page='/') if request.user.is_authenticated()\
            else redirect_with_msg(request, 'You are already logged out.', 'home')


class RelogView(generic.View):

    def dispatch(self, request, *args, **kwargs):
        request.session['Message'] = 'Logged '


class ProfileView(common.views.DetailView):
    template_name = "profilepage.html"
