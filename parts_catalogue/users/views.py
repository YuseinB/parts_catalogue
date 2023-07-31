from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_public_page')  # Редирект след успешна регистрация
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('my_public_page')  # Редирект след успешно логинване
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')