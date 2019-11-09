from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from users.forms import CustomUserCreationForm, CustomUserAuthenticationForm


# LOGIN VIEW: https://www.youtube.com/watch?v=tTvSl3RHBjE
def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('events_list')

    if request.POST:
        form = CustomUserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('events_list')
    else:
        form = CustomUserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


"""Custom User Registration Django
https://www.youtube.com/watch?v=oZUb372g6Do
"""


def register(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('events_list')

    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            new_user = authenticate(email=email, password=raw_password)
            login(request, new_user)
            return redirect('events_list')
        else:
            context['registration_form'] = form
    else:
        form = CustomUserCreationForm()
        context['registration_form'] = form
    return render(request, 'users/register.html', context)
