from django.contrib import auth
from django.shortcuts import render

# Create your views here.
from django.views import generic
from cep15sem2finalproj import common
from cep15sem2finalproj.common.views import redirect_with_msg


class LoginView(common.views.FormView):

    def dispatch(self, request, *args, **kwargs):
        return redirect_with_msg(request, 'You are already logged in.', 'main_index',
                                 permanent=False, *args, **kwargs)


class LogoutView(generic.View):

    def dispatch(self, request, *args, **kwargs):
        request.session['Message'] = 'Logged out successfully.' if request.user.is_authenticated() else None

        return auth.views.logout(request, next_page='/') if request.user.is_authenticated()\
            else redirect_with_msg(request, 'You are already logged out.', 'main_index')
