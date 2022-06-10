import re
import requests


def hot_place(place):
    client_id = "IDEZlxRWK9_vy7ZmJbtf"
    client_secret = "ofIrQU9z72"
    url = f"https://openapi.naver.com/v1/search/local.json?query={place}%20%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&display=5"
    res = requests.get(url, headers={"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    i = 1
    cleanr = re.compile('<.*?>')
    if res.ok:
        data_list = res.json()["items"]
        for data in data_list:
            data['rank'] = i
            data['title'] = re.sub(cleanr, '', data['title'])
            data['image'] = image(data['title'])
            data['category'] = data['category'].split('>')[1]
            i += 1
        return data_list


def search(query):
    client_id = "IDEZlxRWK9_vy7ZmJbtf"
    client_secret = "ofIrQU9z72"
    url = f"https://openapi.naver.com/v1/search/local.json?query={query}"
    res = requests.get(url, headers={"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    cleanr = re.compile('<.*?>')
    if res.ok:
        data = res.json()["items"][0]
        data['title'] = re.sub(cleanr, '', data['title'])
        data['image'] = image(data['title'])
        data['category'] = data['category'].split('>')[1]
        return data


def place_search(query):
    client_id = "IDEZlxRWK9_vy7ZmJbtf"
    client_secret = "ofIrQU9z72"
    url = f"https://openapi.naver.com/v1/search/local.json?query={query}&display=5"
    res = requests.get(url, headers={"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    cleanr = re.compile('<.*?>')
    if res.ok:
        datas = res.json()["items"]
        print(len(datas))
        for data in datas:
            data['title'] = re.sub(cleanr, '', data['title'])
            data['image'] = image(data['title'])
            data['category'] = data['category'].split('>')[1]
        return datas


def image(query):
    client_id = "IDEZlxRWK9_vy7ZmJbtf"
    client_secret = "ofIrQU9z72"
    url = f"https://openapi.naver.com/v1/search/image?query={query}&display=5"
    res = requests.get(url, headers={"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    if res.ok:
        data = res.json()["items"]
        if len(data) == 0:
            link = ""
        else:
            link = res.json()["items"][0]['link']
        return link


def seoul_place():
    data_list = []
    regions = ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구",
               "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구",
               "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구",
               "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"]
    for region in regions:
        data_list += hot_place(region)
    return data_list