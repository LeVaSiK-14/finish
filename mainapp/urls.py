from django.urls import path
from . import views
from .views import UserOneCListView
from django.contrib.auth import views as v


urlpatterns = [
    path('index/', views.index, name="index"),
    path('users/', views.UserOneCListView.as_view()),
    path('send_form/', views.send_form, name="send_form"),
    path('succsess_form/', views.succsess_form, name="succsess_form"),
 	path('logout/', v.LogoutView.as_view(), name='logout'),
 	path('', v.LoginView.as_view(), name='login'),

 	path('Current_month/', views.success_allper, name = 'success_allper'),
 	path('Last_month/', views.succsess_week, name = 'success_week'),
	path('Current_week', views.success_month, name = 'success_month'),
	path('Last_week', views.success_lastweek, name = 'success_lastweek'),

    path('succ/', views.succ, name="succ"),
    path('add/',views.AddAlumno.as_view(),name='alumno-add'),
]
