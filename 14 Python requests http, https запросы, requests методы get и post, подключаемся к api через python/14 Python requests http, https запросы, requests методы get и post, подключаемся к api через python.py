import requests
from apikey import API_TOKEN
# узнаём погоду в одессе :
# params = {"q" : "Одесса", "appid" : API_TOKEN, "units" : "metric"}
# response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

# 200-300 - это успешный ответ от сайта
# 300-400 - было перенаправление (на другую стр. сайта)
# 400-500 ошибка на нашей стороне (например 404 "стр.не найдена")
# 500-600 ошибка на стороне сервера (сайт не работает и т.д.)

#пример get запроса (с подменой внешности(как будто из браузера а не из моей проги пришёл))
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Referer": "http://httpbin.org/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-62791f8c-03152d0f0a7f1bed429afa1a"
  }
#response = requests.get("http://httpbin.org/headers", headers=headers)

#пример post запроса
data = {"custname": "Дзеба Виктор",
"custtel": "0987182314",
"custemail": "frizmob@gmail.com",
"size": "medium",
"topping": "bacon",
"delivery": "",
"comments": "",}
veriable = requests.Session()

aaa = veriable.get("http://httpbin.org/form/post")
response = veriable.post("http://httpbin.org/post", headers=headers, data=data, allow_redirects=True)

# print(response.headers)
# print(response.status_code)
# print(response.content)
# print(response.text)#тот же контент(тело сайта) (только в читабельном виде)




