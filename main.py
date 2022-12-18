import requests
import json
from urllib.parse import urlparse
# bit.ly/3W2dawO
# https://bit.ly/3PxbZ6w

my_header = {"Authorization": "Bearer 66329058b718fde6420ae084eab0e5c4206da0f7"}
url = "https://api-ssl.bitly.com/v4/"
urls = [url + "shorten",url + 'user',url + "bitlinks/"]
url0 = input("Введите текст: \n >-https://") 
data = {}

def is_bitlink(url):
  print(urls[2]+url + '/')
  response = requests.get(urls[2]+url + '/', headers = my_header)
  if response.status_code == 404:
    print(0)
    return True
  print(1)
  return False

def shorten_link(token, url):
  data = {}
  data['long_url'] =  url0 + '/'
  data = json.dumps(data)
  my_json = requests.get(urls[1], headers = my_header).json()
  response = requests.post(urls[0], headers = my_header, data = data, json = my_json)
  if not response.ok:
    raise requests.exceptions.HTTPError(response=response)
  my_json = json.loads(response.text)
  bitlink = my_json["link"]
  return bitlink

def count_clicks(token, url):
  response = requests.get(urls[2]+url, headers = token, params = data_bitlink)
  if not response.ok:
    raise requests.exceptions.HTTPError(response=response)
  return json.loads(urlparse(response.text).path)["total_clicks"]


if is_bitlink(url0): 
  url = "https://" + url0 + "/clicks/summary"
  data_bitlink ={"unit": "day","units":-1}
  try:
    total_clicks = count_clicks(my_header, url)
    print("Количество кликов: {}".format(total_clicks))
  except requests.exceptions.HTTPError:
    print("Ошибка при вводе битлинка!")
    exit()
else:
  try:
    url0 ="https://"  + url0
    bitlink = shorten_link(my_header, url0)
    print("Битлинк: {}".format(bitlink))
  except requests.exceptions.HTTPError:
    print("Ошибка при вводе ссылки!")
    exit()
    
