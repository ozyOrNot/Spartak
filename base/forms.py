from django.forms import ModelForm
from .models import Sportsman, Anthropometry, Competitions, Career, Indicators
from django.forms import TextInput

class SportsmanForm(ModelForm):
    class Meta:
        model = Sportsman
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Имя'}),
            'second_name': TextInput(attrs={'placeholder': 'Фамилия'}),
            'parent_name': TextInput(attrs={'placeholder': 'Отчество'}),
            'birthday': TextInput(attrs={'placeholder': 'Дата рождения'}),
            'phone_number': TextInput(attrs={'placeholder': 'Номер телефона'}),
            'address': TextInput(attrs={'placeholder': 'Адрес'}),
            'passport': TextInput(attrs={'placeholder': 'Серия и номер паспорта'})
        }

class AnthropometryForm(ModelForm):
    class Meta:
        model = Anthropometry
        fields = ['height', 'weight', 'time']

        widgets = {
            'height': TextInput(attrs={'placeholder': 'Рост'}),
            'weight': TextInput(attrs={'placeholder': 'Вес'}),
            'time': TextInput(attrs={'placeholder': 'Дата замера'}),
        }

class CompetitionsForm(ModelForm):
    class Meta:
        model = Competitions
        fields = ['name', 'result', 'time']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Название соревнования'}),
            'result': TextInput(attrs={'placeholder': 'Результат'}),
            'time': TextInput(attrs={'placeholder': 'Дата проведения'}),
        }

class CareerForm(ModelForm):
    class Meta:
        model = Career
        fields = ['team_name', 'position', 'start', 'end']

        widgets = {
            'team_name': TextInput(attrs={'placeholder': 'Название команды'}),
            'position': TextInput(attrs={'placeholder': 'Позиция на льду'}),
            'start': TextInput(attrs={'placeholder': 'Начало работы в клубе'}),
            'end': TextInput(attrs={'placeholder': 'Конец работы в клубе'}),
        }

class IndicatorsForm(ModelForm):
    class Meta:
        model = Indicators
        fields = ['name', 'result', 'time']

        widgets = {
            'result': TextInput(attrs={'placeholder': 'Результат (мера измерения указана в названии норматива)'}),
            'time': TextInput(attrs={'placeholder': 'Дата замера'}),
        }