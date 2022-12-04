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

    return render(request, 'login_page.html')

def logoutUser(request):
    logout(request)
    return redirect('login_page')

def sportmanProfile(request, pk):
    sportman = Sportsman.objects.get(id=pk)
    sportman_form = SportsmanForm(instance=sportman)

    # Изменение общей информации о спортсмене
    if request.method == 'POST':
        sportman.name = request.POST.get("name")
        sportman.second_name = request.POST.get("second_name")
        sportman.parent_name = request.POST.get("parent_name")
        sportman.birthday = request.POST.get("birthday")
        sportman.phone_number = request.POST.get("phone_number")
        sportman.address = request.POST.get("address")
        sportman.passport = request.POST.get("passport")
        sportman.save()
        return redirect('sportman-profile', str(sportman.id))

    context = {'sportman':sportman, 'sportman_form':sportman_form}
    return render(request, 'profile.html', context)

def sportmanAnthropometry(request, pk):
    sportman = Sportsman.objects.get(id=pk)
    context = {'sportman':sportman}
    return render(request, 'profile-anthropometry.html', context)
    