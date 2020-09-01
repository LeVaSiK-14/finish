from django.db import models
from django.contrib.auth.models import User

class UserOneC(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usernameforonec = models.CharField(max_length=64, verbose_name='Имя пользователя 1С')
    passwordforonec = models.CharField(max_length=64, verbose_name='Пароль пользователя 1С')
    wayforbd = models.CharField(max_length=128, verbose_name='Путь к базе данных')
    userid = models.CharField(max_length=64, verbose_name='Id пользователя')

    def __str__(self):
        return self.usernameforonec

    class Meta:
        ordering = ['user']
        verbose_name = 'user'
        verbose_name_plural = 'users'

class FormToOneC(models.Model):
    wayforbd = models.CharField(max_length=500, verbose_name='Путь к базе данных', default='')
    comments = models.TextField('Comment', default='', blank=True)
    usernameonec = models.CharField('UserName', max_length = 500, default='')
    passwordforonec2 = models.CharField(max_length=64, verbose_name='Пароль пользователя 1С', default ='')
    userid2 = models.CharField('ID', max_length=200, default='')
    workobj = models.CharField('Тип работы',max_length=1000, blank=True) 
    job2 = models.CharField('Работа',max_length=1000, default='')
    time2 = models.IntegerField('Время',default='')
    kol2 = models.IntegerField('Количество',default='')

    def __str__(self):
        return self.workobj


class AllPer(models.Model):
    wayforbd = models.CharField(max_length=500, verbose_name='Путь к базе данных', default='')
    iduser = models.CharField('iduser', max_length=500, default='')
    username = models.CharField('username', max_length=500, default='')
    password = models.CharField('password', max_length=500, default='')
    allperiod = models.CharField('All', max_length=500)

    def __str__(self):
        return self.iduser

class Week(models.Model):
    wayforbd = models.CharField(max_length=500, verbose_name='Путь к базе данных', default='')
    username = models.CharField('username', max_length=500, default='')
    password = models.CharField('password', max_length=500, default='')
    iduser = models.CharField('iduser', max_length=500, default='')
    week = models.CharField('week', max_length=500)


    def __str__(self):
        return self.iduser

class Month(models.Model):
    wayforbd = models.CharField(max_length=500, verbose_name='Путь к базе данных', default='')
    username = models.CharField('username', max_length=500, default='')
    password = models.CharField('password', max_length=500, default='')
    iduser = models.CharField('iduser', max_length=500)
    month = models.CharField('month', max_length=500)

    def __str__(self):
        return self.iduser

class LastWeek(models.Model):
    wayforbd = models.CharField(max_length=500, verbose_name='Путь к базе данных', default='')
    username = models.CharField('username', max_length=500, default='')
    password = models.CharField('password', max_length=500, default='')
    iduser = models.CharField('iduser', max_length=500)
    lastweek = models.CharField('LastWeek', max_length=500)

    def __str__(self):
        return self.iduser

# class MultiFormOneC(models.Model):
#     formtoonec = models.ForeignKey(FormToOneC, on_delete=models.CASCADE)
#     job2 = models.CharField(max_length=256, blank=True, null=True)
#     time2 = models.CharField(max_length=8, blank=True, null=True)
#     kol2 = models.CharField(max_length=8, blank=True, null=True)

#     def __str__(self):
#         return self.job2 