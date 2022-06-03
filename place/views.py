from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from naver_api import search
from place.forms import CommentForm
from place.models import Place


def detail(request, region):
    place = search(region)

    exist = Place.objects.filter(title=place['title'])
    if not exist:
        Place.objects.create(title=place['title'], address=place['address'] , roadAddress=place['roadAddress'] , category=place['category'] , image=place['image'] , website=place['link'] , mapx=place['mapx'] , mapy=place['mapy'] )
    data = Place.objects.get(title=place['title'])
    context = {'data':data, 'comment_form':CommentForm}
    return render(request, 'place/detail.html', context)

def new_comment(request, region):
    if request.user.is_authenticated:
        place = get_object_or_404(Place, title=region)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.place = place
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
            else:
                return redirect(place.get_absolute_url())
        else:
            raise PermissionDenied