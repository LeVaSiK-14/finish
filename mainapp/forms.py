from django import forms
from .models import UserOneC, FormToOneC, AllPer, Week, Month, LastWeek
from django.forms import ModelForm




class UserOneCListForm(ModelForm):
    class Meta:
        model = UserOneC
        fields = ['usernameforonec', 'passwordforonec', 'wayforbd', 'userid']

class FormToOneCForm(ModelForm):
    class Meta:
        model = FormToOneC
        fields = ['wayforbd','usernameonec','comments','passwordforonec2','userid2','workobj', 'job2', 'time2', 'kol2',]

class AllPerForm(ModelForm):
	class Meta:
		model = AllPer
		fields = ['wayforbd','password','username','iduser','allperiod']

class WeekForm(ModelForm):
	class Meta:
		model = Week
		fields = ['wayforbd','password','username','iduser','week']

class MonthForm(ModelForm):
	class Meta:
		model = Month
		fields = ['wayforbd','password','username','iduser', 'month']


class LastWeekForm(ModelForm):
	class Meta:
		model = LastWeek
		fields = ['wayforbd','password','username','iduser', 'lastweek']



