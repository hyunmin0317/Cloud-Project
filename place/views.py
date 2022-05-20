from django.shortcuts import render
from naver_api import search
from place.models import Place


def detail(request, region):
    place = search(region)

    exist = Place.objects.filter(title=place['title'])
    if not exist:
        Place.objects.create(title=place['title'], address=place['address'] , roadAddress=place['roadAddress'] , category=place['category'] , image=place['image'] , website=place['link'] , mapx=place['mapx'] , mapy=place['mapy'] )
    data = Place.objects.get(title=place['title'])
    context = {'data':data}
    return render(request, 'place/detail.html', context)
