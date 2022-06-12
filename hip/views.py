from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render, get_object_or_404

from hip.models import Profile
from naver_api import hot_place

def home(request):
    if request.user.is_authenticated:
        exist = Profile.objects.filter(user=request.user)
        if not exist:
            Profile.objects.create(user=request.user)

    region = '서울'
    profiles = Profile.objects.all()

    context = {"region": region, "data_list": hot_place(region), "profiles":profiles}
    return render(request, 'hip/home.html', context)


def detail(request, region):
    profiles = Profile.objects.all()
    context = {"region": region, "data_list": hot_place(region), "profiles":profiles}
    return render(request, 'hip/home.html', context)


@login_required()
def myprofile(request, name):
    user = get_object_or_404(User, username=name)
    profile = get_object_or_404(Profile, user=user)
    data_list = user.voter_post.all()
    comment_list = user.comment_set.all()
    context = {"data_list":data_list, 'username':name, 'placecnt':len(data_list), 'commentcnt':len(comment_list), 'profile':profile}
    return render(request, 'hip/profile.html', context)