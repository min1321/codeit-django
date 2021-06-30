# 서버에 요청이 들어왔을 때 어떻게 처리할지에 관련된 로직이 들어가있음
# model.py와 views.py는 가장 핵심이 되는 파일임

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from foods.models import Menu

# Create your views here.


def index(request):
    context = dict()
    today = datetime.today().date()
    menus = Menu.objects.all()
    context['date'] = today
    context['menus'] = menus
    return render(request, 'foods/index.html', context=context)


def food_detail(request, pk):
    context = dict()
    menu = Menu.objects.get(id=pk)
    context['menu'] = menu
    return render(request, 'foods/detail.html', context=context)
