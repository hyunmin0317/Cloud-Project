from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from naver_api import seoul_place, hot_place


def home(request):
    region = '서울'
    context = {"region": region, "data_list": hot_place(region)}
    return render(request, 'hip/home.html', context)


def detail(request, region):
    context = {"region": region, "data_list": hot_place(region)}
    return render(request, 'hip/home.html', context)


@login_required()
def all(request):
    user = request.user
    data_list = user.voter_post.all()
    context = {"data_list":data_list}
    return render(request, 'hip/map.html', context)


def index(request):
    return render(request, 'hip/index.html')