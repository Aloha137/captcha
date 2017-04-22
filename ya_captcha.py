# -*- coding: utf-8 -*- 
from openpyxl import Workbook
import requests
def gif_cap(name_gif,data):
    f =open('/media/nick/ESD-USB/'+name_gif,'wb')
    captcha_v1 = data.text.partition('image form__captcha')[2]
    captcha_v2 = captcha_v1.partition('src="')[2]
    captcha_v3 = captcha_v2.partition('"')[0]
    data = requests.get(captcha_v3)
    f.write(data.content)
    f.close()    



url_yan = 'https://yandex.ru/showcaptcha?retpath=https%3A//yandex.ru/yandsearch%3Fclid%3D2186618%26text%3D%25D0%25BA%25D1%2583%25D0%25BF%25D0%25B8%25D1%2582%2B%25D0%25BD%25D0%25BE%25D1%2581%25D0%25BA%25D0%25B8_f5b2c3001fb261e43dd29e46ffea3005&t=0/1492870003/4e7b9c13a7abe20d58be08bdbe8ac4a0&s=7418001340a52eec09b2cc3955820544'

co = 200
while co<500:
    print(co)
    data = requests.get(url_yan)
    if 'image form__captcha' in data.text:
        gif_cap('yan_cap_l'+str(co),data)
        co +=1


        
   
