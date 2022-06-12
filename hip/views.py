from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from naver_api import hot_place


def home(request):
    region = '서울'
    context = {"region": region, "data_list": hot_place(region)}
    return render(request, 'hip/home.html', context)


def detail(request, region):
    context = {"region": region, "data_list": hot_place(region)}
    return render(request, 'hip/home.html', context)


@login_required()
def all(request, name):
    user = get_object_or_404(User, username=name)
    data_list = user.voter_post.all()
    context = {"data_list":data_list}
    return render(request, 'hip/profile.html', context)