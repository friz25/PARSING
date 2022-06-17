import requests  # для работы с http
from bs4 import BeautifulSoup as BS  # для парсинга

def parse_stopgame():
# Спарсить, с сайта stopgame.ru, все игры с оценкой "изумительно"
# Главная страница>статьи>обзоры>"изумительно"
# https://stopgame.ru/review/new/izumitelno
    page = 1

    while True:
        # получаем содержимое (в r) нужной нам странички stopgame.ru
        r = requests.get("https://stopgame.ru/review/new/izumitelno/p" + str(page))
        # cкармливаем его BeautifulSoup
        html = BS(r.content, 'html.parser')
        
        items = html.select(".items > .article-summary")
        
        if(len(items)):
            for el in items:
                title = el.select('.caption > a')
                print(title[0].text.replace(': Обзор', ''))
            page += 1
        else:
            break

def parce_smartprogress():
    #спарсить https://smartprogress.do/
    # дан список login, password доступов к аккам на сайте
    # (зайти в каждый) (скачать инфу(опыт, лвл)) 
    #*там есть защита (CSRF токен)
    
    s = requests.Session()#начали Сессию (работы с сайтом)
    #получаем CSRF (ключ от сайта)
    auth_html = s.get("https://smartprogress.do/") # получаем содержимое сайта
    auth_bs = BS(auth_html.content, "html.parser") # cкармливаем его BeautifulSoup
    csrf = auth_bs.select("input[name=YII_CSRF_TOKEN]")[0]['value']
    
    print('print(csrf) = ', csrf)
    #входим в акк
    payload = {
        "YII_CSRF_TOKEN": csrf,
        "returnUrl": '/',
        "UserLoginForm[email]": "frizmob@gmail.com",
        "UserLoginForm[password]": "tester123",
        "UserLoginForm[rememberMe]": 1
    }
    
    answ = s.post("https://smartprogress.do/user/login/", data = payload)
    answ_bs = BS(answ.content, "html.parser")  #открытая (только что) страничка акка
    '''
    /\ Вот тут код пошёл по пизде
    не смог зайти на сайт
    '''
    print(answ_bs)
    # print(answ_bs.select("s__hover-container"))
    
    # print("Имя: {}\nУровень: {}\nОпыт: {}".format(
    #     answ_bs.select(".user-menu__name")[0].text.strip(),
    #     answ_bs.select(".user-menu__info-text--lvl")[0].text.strip(),
    #     answ_bs.select(".user-menu__info-text--exp")[0].text.strip()
    #  ))    
    
    
def main():
    parse_stopgame()
    # parce_smartprogress() '''не смог написать прогу пока что'''

if __name__ == '__main__':
    main()

#нужен тест на ссылку 10
#нужен try catch
#нужно всё в функцию
#нужно писать результаты в файл
#(в случае прерывания записи, сохранить те что уже получены и вывести сообщение о причине)

#нужна функция main()
#нужен __name__ = '__main__'

#нужна сборка теста (unittest,pytest,doctest)
#нужно соединение с Git и коммиты этапов работы над проектом