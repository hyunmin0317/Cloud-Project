from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render, get_object_or_404, redirect

from hip.forms import ProfileForm
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


def myprofile(request, name):
    user = get_object_or_404(User, username=name)
    profile = get_object_or_404(Profile, user=user)
    data_list = user.voter_post.all()
    comment_list = user.comment_set.all()
    context = {'users' : user, "data_list":data_list, 'username':name, 'placecnt':len(data_list), 'commentcnt':len(comment_list), 'profile':profile}
    return render(request, 'hip/profile.html', context)


@login_required()
def update(request, name):
    user = get_object_or_404(User, username=name)
    profile = get_object_or_404(Profile, user=user)
    if request.user != user:
        messages.error(request, '수정권한이 없습니다')
        return redirect('hip:profile', name=name)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('hip:profile', name=name)
    else:
        profiles = Profile.objects.all()
        form = ProfileForm(instance=profile)
        context = {'form': form, 'profile':profile, 'profiles':profiles}
        return render(request, 'hip/update.html', context)