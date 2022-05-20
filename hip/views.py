from django.shortcuts import render
from hip.naver_api import hot_place


def home(request):
    context = {"data_list": hot_place("서울")}
    return render(request, 'hip/home.html', context)


def all(request):
    data_list = []
    regions = ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구",
              "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구",
              "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구",
              "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"]
    for region in regions:
        data_list += hot_place(region)
    context = {"data_list":data_list}
    return render(request, 'hip/detail.html', context)


def detail(request, region):
    context = {"region":region, "data_list": hot_place(region)}
    return render(request, 'hip/detail.html', context)

def index(request):
    return render(request, 'hip/index.html')