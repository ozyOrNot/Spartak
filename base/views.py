from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib.auth.models import User
from .models import Sportsman

from .forms import SportsmanForm

@login_required(login_url='login_page')
def home_page(request):
    # Фильрация поиска
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    sportmans = Sportsman.objects.filter(
        Q(name__icontains=q) |
        Q(second_name__icontains=q) |
        Q(parent_name__icontains=q) |
        Q(birthday__icontains=q) |
        Q(phone_number__icontains=q)
        )

    # Добавление спортсмена в бд
    sportman_form = SportsmanForm()
    if request.method == 'POST':
        sportman_form = SportsmanForm(request.POST)
        if sportman_form.is_valid():
            sportman_form.save()
            return redirect('home')

    context = {'sportmans':sportmans, 'sportman_form':sportman_form}
    return render(request, 'home.html', context)

def delete_profile(request, pk):
    sportman = Sportsman.objects.get(id=pk)
    sportman.delete()
    return redirect('home')

def login_page(request):
    # Аутентификация
    if request.method == 'POST':
        # С инпутов принимается информация по атрибуту name
        username = request.POST.get('username')
        password = request.POST.get('password')   
        # Поиск пользователя с идентичным именем
        try:
            user = User.objects.get(username=username)
        except:
            pass
        # Функция аутентификации
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'login_page.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login_page')