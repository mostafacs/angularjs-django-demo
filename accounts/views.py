import django
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms.models import ModelForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from accounts.models import PresentUser
from django.contrib.auth import authenticate, login, logout
from presenter.views import process_after_register

##### For user registration, lets just use the app 
class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = PresentUser
        fields = ('email', 'first_name',)


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = PresentUser
        fields = ('email', 'first_name', )


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = PresentUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'gender',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


def perform_login(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            user = authenticate(username=loginform.cleaned_data['username'],
                                password=loginform.cleaned_data['password'])
            if not user or not user.is_active:
                raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
                return render_to_response('login.html', {'form': loginform}, context_instance=RequestContext(request))
            else:
                login(request, user)
                return redirect('/')
        else:
            return render_to_response('login.html', {'form': loginform}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        return render_to_response(
            'login.html',
            {'form': form},
            context_instance=RequestContext(request)
        )

"""
def social_login(request):
    Home view, displays login mechanism
    if request.user.is_authenticated():
        return redirect('home')
    return context()
"""

def perform_logout(request):
    logout(request)
    return redirect('/')





def register(request):
    if request.method == 'POST':
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            print('Saved...')
            user = authenticate(username=registerform.cleaned_data['email'],
                                password=registerform.cleaned_data['password1'])
            login(request, user)
            return redirect('/process/login')
    else:
        registerform = RegisterForm()

    return render_to_response(
        'register.html',
        {'form': registerform},
        context_instance=RequestContext(request)
    )


#@csrf_exempt
def token(request):
    print(django.middleware.csrf.get_token(request))
    response = HttpResponse(django.middleware.csrf.get_token(request))
    return response


