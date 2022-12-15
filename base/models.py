from django.db import models
from django.contrib.auth.models import User

class Sportsman(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=300, null=True, blank=True)
    passport = models.CharField(max_length=20)
    photo = models.ImageField(null=True, blank=True, upload_to="sportmen-images/", verbose_name="Изображение")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Anthropometry(models.Model):
    sportman = models.ForeignKey(Sportsman, on_delete=models.CASCADE, null=True)
    height = models.FloatField()
    weight = models.FloatField()
    index = models.FloatField(blank=True, null=True)
    time = models.DateField()

    def __str__(self):
        return f'Anthropometry: {self.sportman.name} {self.sportman.second_name} {self.sportman.parent_name}'

class Competitions(models.Model):
    sportman = models.ForeignKey(Sportsman, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    result = models.CharField(max_length=100)
    time = models.DateField()

    def __str__(self):
        return f'Competition: {self.sportman.name} {self.sportman.second_name} {self.sportman.parent_name} | {self.name}'

class Career(models.Model):
    sportman = models.ForeignKey(Sportsman, on_delete=models.SET_NULL, null=True)
    team_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f'Career: {self.sportman.name} {self.sportman.second_name} {self.sportman.parent_name} | {self.start}-{self.end}'

class Indicators(models.Model):

    INDICATOR_CHOISES = [
        ('Подтягивания на перекладине (кол-во)', 'Подтягивания на перекладине (кол-во)'),
        ('Тройной прыжок с места (см)', 'Тройной прыжок с места (см)'),
        ('Пятикратный прыжок (см)', 'Пятикратный прыжок (см)'),
        ('Поднимание туловища 60 сек. (кол-во)', 'Поднимание туловища 60 сек. (кол-во)'),
        ('Бег 60м (сек)', 'Бег 60м (сек)'),
        ('Бег 300м (сек)', 'Бег 300м (сек)'),
        ('Бег 3000м (мин)', 'Бег 3000м (мин)'),
        ('Бег на коньках 36м лицом вперед (сек)', 'Бег на коньках 36м лицом вперед (сек)'),
        ('Бег на коньках 36м спиной вперед (сек)', 'Бег на коньках 36м спиной вперед (сек)'),
        ('Челночный бег на коньках 18 х 12 м (сек)', 'Челночный бег на коньках 18 х 12 м (сек)'),
        ('8-минутный бег на коньках (км)', '8-минутный бег на коньках (км)'),
        ('Точность бросков шайбы в цель (очки)', 'Точность бросков шайбы в цель (очки)'),
    ]

    sportman = models.ForeignKey(Sportsman, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300, choices=INDICATOR_CHOISES, default='Бег 60м (сек)')
    result = models.CharField(max_length=100)
    time = models.DateField()

    def __str__(self):
        return f'Indicator: {self.sportman.name} {self.sportman.second_name} {self.sportman.parent_name} | {self.name}'

class Medicine(models.Model):
    sportman = models.ForeignKey(Sportsman, on_delete=models.SET_NULL, null=True)
    bpm = models.IntegerField(blank=True, null=True)
    arterial_pressure = models.CharField(max_length=7, blank=True, null=True)
    medical_tests = models.FileField(blank=True, null=True)
    medical_survey = models.FileField(blank=True, null=True)
    time = models.DateField()

    def __str__(self):
        return f'Indicator: {self.sportman.name} {self.sportman.second_name} {self.sportman.parent_name} | {self.time}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    proteins = models.FloatField(max_length=10)
    fats = models.FloatField(max_length=10)
    carbo = models.FloatField(max_length=10)
    calories = models.FloatField(max_length=10)

    def __str__(self):
        return f'{self.name} | {self.calories}'


class Diet(models.Model):
    sportman = models.ForeignKey(Sportsman, on_delete=models.SET_NULL, null=True)
    monday_breakfast = models.TextField(null=True, blank=True)
    monday_lunch = models.TextField(null=True, blank=True)
    monday_dinner = models.TextField(null=True, blank=True)
    monday_calories = models.CharField(max_length=100, null=True, blank=True)
    
    tuesday_breakfast = models.TextField(null=True, blank=True)
    tuesday_lunch = models.TextField(null=True, blank=True)
    tuesday_dinner = models.TextField(null=True, blank=True)
    tuesday_calories = models.CharField(max_length=100, null=True, blank=True)

    wednesday_breakfast = models.TextField(null=True, blank=True)
    wednesday_lunch = models.TextField(null=True, blank=True)
    wednesday_dinner = models.TextField(null=True, blank=True)
    wednesday_calories = models.CharField(max_length=100, null=True, blank=True)
    
    thursday_breakfast = models.TextField(null=True, blank=True)
    thursday_lunch = models.TextField(null=True, blank=True)
    thursday_dinner = models.TextField(null=True, blank=True)
    thursday_calories = models.CharField(max_length=100, null=True, blank=True)

    friday_breakfast = models.TextField(null=True, blank=True)
    friday_lunch = models.TextField(null=True, blank=True)
    friday_dinner = models.TextField(null=True, blank=True)
    friday_calories = models.CharField(max_length=100, null=True, blank=True)

    saturday_breakfast = models.TextField(null=True, blank=True)
    saturday_lunch = models.TextField(null=True, blank=True)
    saturday_dinner = models.TextField(null=True, blank=True)
    saturday_calories = models.CharField(max_length=100, null=True, blank=True)
    
    sunday_breakfast = models.TextField(null=True, blank=True)
    sunday_lunch = models.TextField(null=True, blank=True)
    sunday_dinner = models.TextField(null=True, blank=True)
    sunday_calories = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.sportman.name}'

class Trauma(models.Model):
    sportman = models.ForeignKey(Sportsman, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    file = models.FileField(blank=True, null=True)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f'{self.name} | {self.start} - {self.end}'
