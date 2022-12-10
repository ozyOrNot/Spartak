from django.forms import ModelForm
from .models import Sportsman, Anthropometry, Competitions
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