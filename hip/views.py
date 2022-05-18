from django.shortcuts import render
from hip.naver_api import hot_place

def home(request):
    context = {"data_list":hot_place("서울")}
    return render(request, 'home.html', context)