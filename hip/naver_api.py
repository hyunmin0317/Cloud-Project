import urllib.request
import requests


def hot_place(place):
    url = f'https://map.naver.com/v5/api/search?query={place}%20%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&displayCount=100'
    res = requests.get(url, headers={'authority': 'map.naver.com'}).json()
    data_list = res['result']['place']['list']
    return data_list


def search(query):
    client_id = "IDEZlxRWK9_vy7ZmJbtf"
    client_secret = "ofIrQU9z72"
    encText = urllib.parse.quote(query)
    url = "https://openapi.naver.com/v1/search/local.json?query=" + encText  # json 결과

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)



def image(query):
    client_id = "IDEZlxRWK9_vy7ZmJbtf"
    client_secret = "ofIrQU9z72"
    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/image?query={encText}&display=1"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

hot_place('서울')
# search('롯데월드')
# image('롯데월드')