#https://www.figma.com/proto/74HDae8yvzq0F9w0KPATIl/opt-project-number?node-id=61%3A135&scaling=fit-width
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
import json
import requests
from .forms import UserOneCListForm, FormToOneCForm, WeekForm, MonthForm, AllPerForm, LastWeekForm
from django.urls import reverse
from .models import UserOneC, FormToOneC
from .serializers import UserOneCListSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import formset_factory, modelformset_factory
from django.views.generic.edit import FormView
import requests
from django.urls import reverse_lazy


def index(request):
    template_name = '../templates/mainapp/index.html'
    return render(request, template_name)

class UserOneCListView(APIView):
    def get(self, request):
        user_one_c = UserOneC.objects.filter()
        serializer = UserOneCListSerializer(user_one_c, many=True)
        return Response(serializer.data)

def send_form(request):
    template_name = '../templates/mainapp/send_form.html'
    users = UserOneC.objects.all()
    context = {
    'users' : users,
    }
    return render(request, template_name, context)


def succsess_form(request):
    username=''
    password=''
    URL_LOG=''
    userid=''
    if request.method == "GET":
        form = UserOneCListForm(request.GET or None)
        if form.is_valid():
            username= form.cleaned_data.get("usernameforonec")
            password= form.cleaned_data.get("passwordforonec")
            URL_LOG= form.cleaned_data.get("wayforbd")
            userid = form.cleaned_data.get("userid")
        
            data = {
                    'username': username,
                    'password': password,
                    'userid': userid,
                    }


            r1 = requests.get(URL_LOG + '/hs/tid/getdata', data=data, auth=(username, password))

            file_name = 'post_settings.txt'
            my_data = open(file_name, mode = 'w', encoding="utf-8")
            myjson = r1.json()
            json.dump(myjson, my_data)
            my_data.close()
            return redirect('/add/')



def succ(request):
    return render(request, 'mainapp/suc.html')


class AddAlumno(FormView):
    template_name = 'mainapp/add.html'
    form_class = formset_factory(FormToOneCForm, extra=1)
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(AddAlumno, self).get_context_data(**kwargs)
        template_name = 'mainapp/form.html'
        f = open('post_settings.txt')
        fd = f.read()
        file = json.loads(fd)

        workobjf = []
        jobf = []
        for i in file[0]:
            ii = i['Name']
            iii = i['Code']
            workobjf.append(ii + ',' + iii)
            



        for i in file[1]:
            ii = i['Name']
            iii = i['Code']
            jobf.append(ii + ',' + iii)

        context['workobj'] = workobjf
        context['job'] = jobf
        return context

    def form_valid(self, form):
        dictform = []


        for f in form:

            url = f.cleaned_data['wayforbd']
            usernameonec2 = f.cleaned_data['usernameonec']
            comment = f.cleaned_data['comments']
            password = f.cleaned_data['passwordforonec2']
            id2 = f.cleaned_data['userid2']
            workobj2 = f.cleaned_data['workobj']
            job2 = f.cleaned_data['job2']
            time2 = f.cleaned_data['time2']
            kol2 = f.cleaned_data['kol2']

            workobj3 = workobj2.split(',')[-1]
            job3 = job2.split(',')[-1]

            dictform.append(workobj3)
            dictform.append(job3)
            dictform.append('Time: ' + str(time2))
            dictform.append('Quality: ' + str(kol2))
            dictform.append('Comment: ' + comment)

            payloads = {
                'UserName': usernameonec2,
                'UserID': id2,
                'worklist': dictform,

            }

            #print(payloads)

            file_name2 = 'form.txt'
            my_data2 = open(file_name2, mode = 'w', encoding="utf-8")
            json.dump(payloads, my_data2)
            my_data2.close()


            r = requests.post(url + '/hs/tid/setdata', data=json.dumps(payloads), auth =(usernameonec2, password))
            #Чтобы проверить успешно ли отправен запрос
            #print(r)


            #f.save()

        return super(AddAlumno, self).form_valid(form)

#s = 'HELLO WORLD'
#payloads = {'message': s}
#r = requests.post(url, data=json.dumps(payloads))

def success_allper(request):
    if request.method == "POST":
        form = AllPerForm(request.POST or None)
        if form.is_valid():
            url = form.cleaned_data.get('wayforbd')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            iduser = form.cleaned_data.get('iduser')
            allper= form.cleaned_data.get("allperiod")
        
            data = {
                    'UserID': iduser,
                    'ID': allper,
                    }

            r1 = requests.get(url +'/hs/tid/report', data=json.dumps(data), auth=(username, password))
            #file_name2 = 'all.txt'
            #my_data2 = open(file_name2, mode = 'w',encoding="utf-8")
            #json.dump(data, my_data2)
            #my_data2.close()
            response = HttpResponse(r1, content_type='application/pdf')

            return response




def succsess_week(request):
    if request.method == "POST":
        form = WeekForm(request.POST or None)
        if form.is_valid():
            url = form.cleaned_data.get('wayforbd')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            iduser = form.cleaned_data.get('iduser')
            week= form.cleaned_data.get("week")
        
            data = {
                    'UserID': iduser,
                    'ID':week,
                    }

            r1 = requests.get(url +'/hs/tid/report', data=json.dumps(data), auth=(username, password))
            #file_name2 = 'week.txt'
            #my_data2 = open(file_name2, mode = 'w', encoding="utf-8")
            #json.dump(data, my_data2)
            #my_data2.close()
            response = HttpResponse(r1, content_type='application/pdf')

            return response



def success_month(request):
    if request.method == "POST":
        form = MonthForm(request.POST or None)
        if form.is_valid():
            url = form.cleaned_data.get('wayforbd')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            iduser = form.cleaned_data.get('iduser')
            month= form.cleaned_data.get("month")
        
            data = {
                    'UserID': iduser,
                    'ID': month,
                    }

            r1 = requests.get(url +'/hs/tid/report', data=json.dumps(data), auth=(username, password))
            #file_name2 = 'month.txt'
            #my_data2 = open(file_name2, mode = 'w', encoding="utf-8")
            #json.dump(data, my_data2)
            #my_data2.close()
            response = HttpResponse(r1, content_type='application/pdf')

            return response

def success_lastweek(request):
    if request.method == "POST":
        form = LastWeekForm(request.POST or None)
        if form.is_valid():
            url = form.cleaned_data.get('wayforbd')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            iduser = form.cleaned_data.get('iduser')
            lastweek= form.cleaned_data.get("lastweek")
        
            data = {
                    'UserID': iduser,
                    'ID': lastweek,
                    }

            r1 = requests.get(url +'/hs/tid/report', data=json.dumps(data), auth=(username, password))
            #file_name2 = 'month.txt'
            #my_data2 = open(file_name2, mode = 'w', encoding="utf-8") 
            #json.dump(data, my_data2)
            #my_data2.close()
            response = HttpResponse(r1, content_type='application/pdf')

            return response
