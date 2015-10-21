from django.contrib import auth
from django.contrib.auth import views as authviews, authenticate, login
from django.shortcuts import render
from . import models

# Create your views here.
from django.views import generic
from cep15sem2finalproj import common
from cep15sem2finalproj.common.views import redirect_with_msg
from . import forms


class LoginView(common.views.FormView):

    template_name = 'loginpage.html'

    def dispatch(self, request, *args, **kwargs):
        return redirect_with_msg(request, 'You are already logged in.', 'home', permanent=False, *args, **kwargs) \
            if request.user.is_authenticated() else authviews.login(request, template_name='loginpage.html', extra_context={'user': models.UserProfile.get(self.request.user)})


class LogoutView(generic.View):

    def dispatch(self, request, *args, **kwargs):
        request.session['Message'] = 'Logged out successfully.' if request.user.is_authenticated() else None

        return authviews.logout(request, next_page='/') if request.user.is_authenticated()\
            else redirect_with_msg(request, 'You are already logged out.', 'home')


class RelogView(generic.View):

    def dispatch(self, request, *args, **kwargs):
        request.session['Message'] = 'Logged '


class RegisterView(generic.TemplateView):
    template_name = 'registration.html'
    app = 'home'

    user_form = forms.UserForm
    profile_form = forms.UserProfileForm

    def get(self, request, *args, **kwargs):
        kwargs.setdefault('user_form', self.user_form())
        kwargs.setdefault('profile_form', self.profile_form())
        return super(RegisterView, self).get(request, *args, app='home', **kwargs)

    def post(self, request, *args, **kwargs):
        user_form = self.user_form(data=request.POST)
        profile_form = self.profile_form(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            user = authenticate(username=request.POST.get('username'),
                                password=request.POST.get('password1'))
            login(request, user)
            return redirect_with_msg(request, 'Welcome!', 'main_index')

        else:
            return redirect_with_msg(
                request, 'The following errors were found: \n{0} \n{1}'.format(user_form.errors, profile_form.errors),
                'register'
            )


class ProfileView(common.views.DetailView):
    template_name = "profilepage.html"
