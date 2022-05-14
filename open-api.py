import requests

url = 'https://map.naver.com/v5/api/search?query=%EC%84%9C%EC%9A%B8%20%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&displayCount=100'
res = requests.get(url, headers={'authority': 'map.naver.com'}).json()
data_list = res['result']['place']['list']

for data in data_list:
    print(data)