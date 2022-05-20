from django.shortcuts import render
from hip.naver_api import seoul_place, preprocess


def home(request):
    region = '서울'
    context = {"region": region, "data_list": preprocess(region)}
    return render(request, 'hip/home.html', context)


def detail(request, region):
    context = {"region": region, "data_list": preprocess(region)}
    return render(request, 'hip/home.html', context)


def all(request):
    context = {"data_list":seoul_place()}
    return render(request, 'hip/map.html', context)


def index(request):
    return render(request, 'hip/index.html')