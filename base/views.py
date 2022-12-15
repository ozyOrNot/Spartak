from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib.auth.models import User
from .models import Sportsman, Anthropometry, Competitions, Career, Indicators, Medicine, Product, Diet, Trauma

from .forms import SportsmanForm, AnthropometryForm, CompetitionsForm, CareerForm, IndicatorsForm, MedicineForm, DietForm, TraumaForm

@login_required(login_url='login_page')
def home_page(request):
    # Фильрация поиска
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    sportmans = Sportsman.objects.filter(
        Q(name__icontains=q) |
        Q(second_name__icontains=q) |
        Q(parent_name__icontains=q) |
        Q(birthday__icontains=q) |
        Q(phone_number__icontains=q) |
        Q(id__icontains=q)
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

def compare_page(request):
    context = {}
    return render(request, 'compare.html', context)

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
        sportman.photo = request.FILES.get("photo")
        sportman.save()
        return redirect('sportman-profile', str(sportman.id))

    context = {'sportman':sportman, 'sportman_form':sportman_form}
    return render(request, 'profile.html', context)

def sportmanAnthropometry(request, pk):
    sportman = Sportsman.objects.get(id=pk)
    anthropometries = Anthropometry.objects.filter(sportman=sportman)

    anthropometry_form = AnthropometryForm()
    if request.method == 'POST':
        anthropometry_form = AnthropometryForm(request.POST)
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        if anthropometry_form.is_valid():
            commit_form = anthropometry_form.save(commit=False)
            commit_form.sportman = sportman
            commit_form.index = float(height) * float(weight)
            commit_form.save()

    context = {'sportman':sportman, 'anthropometries':anthropometries, 'anthropometry_form':anthropometry_form}
    return render(request, 'profile-anthropometry.html', context)

def sportmanCompetitions(request, pk):
    sportman = Sportsman.objects.get(id=pk)
    competitions = Competitions.objects.filter(sportman=sportman)

    competition_form = CompetitionsForm()
    if request.method == 'POST':
        competition_form = CompetitionsForm(request.POST)
        if competition_form.is_valid():
            form = competition_form.save(commit=False)
            form.sportman = sportman
            form.save()
            return redirect('sportman-competitions', str(sportman.id))

    context = {'sportman':sportman, 'competitions':competitions, 'competition_form':competition_form}
    return render(request, 'profile_competition.html', context)

def sportmanCareer(request, pk):
    sportman = Sportsman.objects.get(id=pk)
    career_history = Career.objects.filter(sportman=sportman)

    career_form = CareerForm()
    if request.method == 'POST':
        career_form = CareerForm(request.POST)
        if career_form.is_valid():
            form = career_form.save(commit=False)
            form.sportman = sportman
            form.save()
            return redirect('sportman-career', str(sportman.id))

    context = {'sportman':sportman, 'career_history':career_history, 'career_form':career_form}
    return render(request, 'profile-career.html', context)

def sportmanIndicators(request, pk):
    sportman = Sportsman.objects.get(id=pk)
    indicators = Indicators.objects.filter(sportman=sportman)

    indicators_form = IndicatorsForm()
    if request.method == 'POST':
        indicators_form = IndicatorsForm(request.POST)
        if indicators_form.is_valid():
            form = indicators_form.save(commit=False)
            form.sportman = sportman
            form.save()
            return redirect('sportman-indicators', str(sportman.id))

    context = {'sportman':sportman, 'indicators':indicators, 'indicators_form':indicators_form}
    return render(request, 'profile-indicators.html', context)

def sportmanMedicine(request, pk):
    sportman = Sportsman.objects.get(id=pk)
    medicine_tests = Medicine.objects.filter(sportman=sportman)

    medicine_form = MedicineForm()
    if request.method == 'POST':
        medicine_form = MedicineForm(request.POST, request.FILES)
        if medicine_form.is_valid():
            form = medicine_form.save(commit=False)
            form.sportman = sportman
            form.save()
            return redirect('sportman-medicine', str(sportman.id))

    context = {'sportman':sportman, 'medicine_tests':medicine_tests, 'medicine_form':medicine_form}
    return render(request, 'profile_medicine.html', context)

def sportmanDiet(request, pk):
    sportman = Sportsman.objects.get(id=pk)

    try:
        diet = Diet.objects.get(sportman=sportman)
        diet_form = DietForm(instance=diet)

        if request.method == 'POST':
            diet.monday_breakfast = request.POST.get('monday_breakfast')
            diet.monday_lunch = request.POST.get('monday_lunch')
            diet.monday_dinner = request.POST.get('monday_dinner')
            diet.monday_calories = request.POST.get('monday_calories')

            diet.tuesday_breakfast = request.POST.get('tuesday_breakfast')
            diet.tuesday_lunch = request.POST.get('tuesday_lunch')
            diet.tuesday_dinner = request.POST.get('tuesday_dinner')
            diet.tuesday_calories = request.POST.get('tuesday_calories')

            diet.wednesday_breakfast = request.POST.get('wednesday_breakfast')
            diet.wednesday_lunch = request.POST.get('wednesday_lunch')
            diet.wednesday_dinner = request.POST.get('wednesday_dinner')
            diet.wednesday_calories = request.POST.get('wednesday_calories')

            diet.thursday_breakfast = request.POST.get('thursday_breakfast')
            diet.thursday_lunch = request.POST.get('thursday_lunch')
            diet.thursday_dinner = request.POST.get('thursday_dinner')
            diet.thursday_calories = request.POST.get('thursday_calories')

            diet.friday_breakfast = request.POST.get('friday_breakfast')
            diet.friday_lunch = request.POST.get('friday_lunch')
            diet.friday_dinner = request.POST.get('friday_dinner')
            diet.friday_calories = request.POST.get('friday_calories')

            diet.saturday_breakfast = request.POST.get('saturday_breakfast')
            diet.saturday_lunch = request.POST.get('saturday_lunch')
            diet.saturday_dinner = request.POST.get('saturday_dinner')
            diet.saturday_calories = request.POST.get('saturday_calories')

            diet.sunday_breakfast = request.POST.get('sunday_breakfast')
            diet.sunday_lunch = request.POST.get('sunday_lunch')
            diet.sunday_dinner = request.POST.get('sunday_dinner')
            diet.sunday_calories = request.POST.get('sunday_calories')

            diet.save()
            return redirect('sportman-diet', str(sportman.id))

        context = {'sportman':sportman, 'diet':diet, 'diet_form':diet_form}
        return render(request, 'profile-diet.html', context)
    except:
        diet_form = DietForm()

    if request.method == 'POST':
        diet_form = DietForm(request.POST)
        if diet_form.is_valid():
            form = diet_form.save(commit=False)
            form.sportman = sportman
            form.save()
            return redirect('sportman-diet', str(sportman.id))
            
        context = {'sportman':sportman, 'diet_form':diet_form}
        return render(request, 'profile-diet.html', context)

def sportmanTrauma(request, pk):
    sportman = Sportsman.objects.get(id=pk)
    traumas = Trauma.objects.filter(sportman=sportman)

    trauma_form = TraumaForm()
    if request.method == 'POST':
        trauma_form = TraumaForm(request.POST, request.FILES)
        if trauma_form.is_valid():
            form = trauma_form.save(commit=False)
            form.sportman = sportman
            form.save()
            return redirect('sportman-traumas', str(sportman.id))
    
    context = {'sportman':sportman, 'traumas':traumas, 'trauma_form':trauma_form}
    return render(request, 'profile-trauma.html', context)