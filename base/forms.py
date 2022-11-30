from django.forms import ModelForm
from .models import Sportsman
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
            'passport': TextInput(attrs={'placeholder': 'Серия и номер паспорта'})
        }