from django.forms import ModelForm
from .models import Sportsman, Anthropometry, Competitions, Career, Indicators, Medicine, Diet, Trauma
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

class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = ['bpm', 'arterial_pressure', 'medical_tests', 'medical_survey', 'time']

        widgets = {
            'bpm': TextInput(attrs={'placeholder': 'Частота сердцебиения'}),
            'arterial_pressure': TextInput(attrs={'placeholder': 'Артериальное давление'}),
            'time': TextInput(attrs={'placeholder': 'Дата снятия медицинских показателей'}),
        }

class DietForm(ModelForm):
    class Meta:
        model = Diet
        fields = [
            'monday_breakfast', 'monday_lunch', 'monday_dinner', 'monday_calories',
            'tuesday_breakfast', 'tuesday_lunch', 'tuesday_dinner', 'tuesday_calories',
            'wednesday_breakfast', 'wednesday_lunch', 'wednesday_dinner', 'wednesday_calories',
            'thursday_breakfast', 'thursday_lunch', 'thursday_dinner', 'thursday_calories',
            'friday_breakfast', 'friday_lunch', 'friday_dinner', 'friday_calories',
            'saturday_breakfast', 'saturday_lunch', 'saturday_dinner', 'saturday_calories',
            'sunday_breakfast', 'sunday_lunch', 'sunday_dinner', 'sunday_calories',
        ]

class TraumaForm(ModelForm):
    class Meta:
        model = Trauma
        fields = ['name', 'start', 'end', 'file']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Название травмы'}),
            'start': TextInput(attrs={'placeholder': 'Дата получения травмы'}),
            'end': TextInput(attrs={'placeholder': 'Дата окончательного восстановления'}),
        }