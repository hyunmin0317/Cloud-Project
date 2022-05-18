import requests


def hot_place(place):
    client_id = "IDEZlxRWK9_vy7ZmJbtf"
    client_secret = "ofIrQU9z72"
    url = f"https://openapi.naver.com/v1/search/local.json?query={place}%20%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&display=5"
    res = requests.get(url, headers={"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    if res.ok:
        data_list = res.json()["items"]
        return data_list


def search(query):
    client_id = "IDEZlxRWK9_vy7ZmJbtf"
    client_secret = "ofIrQU9z72"
    url = f"https://openapi.naver.com/v1/search/local.json?query={query}"
    res = requests.get(url, headers={"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    if res.ok:
        data_list = res.json()["items"][0]
        return data_list


def image(query):
    client_id = "IDEZlxRWK9_vy7ZmJbtf"
    client_secret = "ofIrQU9z72"
    url = f"https://openapi.naver.com/v1/search/image?query={query}&display=1"
    res = requests.get(url, headers={"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    if res.ok:
        data_list = res.json()["items"][0]['link']
        return data_list