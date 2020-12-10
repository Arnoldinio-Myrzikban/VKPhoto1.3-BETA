import vk_api
import colorama
from colorama import Fore
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll
import time
colorama.init()

banner = ["""
Накрутка Фотографий

ВНИМАНИЕ ВЕРСИЯ БЕТА!

VK Автора: @russian_osint

██████▄▄░░░░░░░░░░░░░░░░░░░░░░░░▄▄██████
███████▀██▄░░░░░░░░░░░░░░░░░░▄██▀███████
░█████░░░░▀█▄░░▄▄▄▄▄▄▄▄▄▄░░▄█▀░░░░█████░
░▀███▀░░░░▄███▀▀▀▀░░░░▀▀▀▀███▄░░░░▀███▀░
░░▀██░░░░░▀▀░░░░░░░░░░░░░░░░▀▀░░░░░██▀░░
░░░▀█▄▄██░░░░░░░░░░░░░░░░░░░░░░██▄▄█▀░░░
░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░
░░░░░░█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█░░░░░░
░░░░░██░░▄▄██▄░░░░░░░░░░░░▄██▄▄░░██░░░░░
░░░░░██░▄█▀░███░░░░░░░░░░███░▀█▄░██░░░░░
░░░░▄█▀░▀█▄▄▄█▀░░░░▄▄░░░░▀█▄▄▄█▀░▀█▄░░░░
░░░░██▄▄▄░▀▀▀░░░░░▀██▀░░░░░▀▀▀░▄▄▄██░░░░
░░░████████░░░▀█▄▄▄██▄▄▄█▀░░░████████░░░
░░░▀████████░░░░░█░░░░█░░░░░████████▀░░░
░░░░▀██████░░░░░░█▄░░▄█░░░░░░██████▀░░░░
░░░░░▀███▀░░░░░░░▀█▄▄█▀░░░░░░░▀███▀░░░░░
░░░░░░░░▀██▄▄░░░░░░▀▀░░░░░░▄▄██▀░░░░░░░░
░░░░░░░░░░░▀▀▀███▄▄▄▄▄▄███▀▀▀░░░░░░░░░░░

Version: 1.3
"""]

print(Fore.YELLOW + banner[0])

token1 = input('Введите Токен Страницы: ')
album = input('Введите ИД альбома: ')

pri = int(-1)

# Введите название фото из папки в скобках
photo1 = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg', 'photo5.jpg']

photo2 = ['photo6.jpg', 'photo7.jpg', 'photo8.jpg', 'photo9.jpg', 'photo10.jpg']

photo3 = ['photo11.jpg', 'photo12.jpg', 'photo13.jpg', 'photo14.jpg', 'photo15.jpg']

photo4 = ['photo16.jpg', 'photo17.jpg', 'photo18.jpg', 'photo19.jpg', 'photo20.jpg']

vk_session = vk_api.VkApi(token=token1)
longpoll = VkLongPoll(vk_session)
upload = VkUpload(vk_session)
vk = vk_session.get_api()


vk_time = int(0)

def photos(n):
    for i in range(len(n)):
        upload.photo(photos=n, album_id=album)


while True:
    try:
        vk_time = vk_time + len(photo1)
        print('Накручено ', vk_time)
        photos(photo1)
        pri = pri + 1
        if vk_time == 450:
            print("Обход капчи ВКонтакте, подождите '2' Минуты!")
            vk_time = int(0)
            time.sleep(120)
        vk_time = vk_time + len(photo2)
        print('Накручено ', vk_time)
        photos(photo2)
        pri = pri + 1
        if vk_time == 450:
            print("Обход капчи ВКонтакте, подождите '2' Минуты!")
            vk_time = int(0)
            time.sleep(120)
        vk_time = vk_time + len(photo3)
        print('Накручено ', vk_time)
        photos(photo3)
        pri = pri + 1
        if vk_time == 450:
            print("Обход капчи ВКонтакте, подождите '2' Минуты!")
            vk_time = int(0)
            time.sleep(120)
        vk_time = vk_time + len(photo4)
        print('Накручено ', vk_time)
        photos(photo4)
        pri = pri + 1
        if vk_time == 450:
            print("Обход капчи ВКонтакте, подождите '2' Минуты!")
            vk_time = int(0)
            time.sleep(120)

    except Exception as error:
        print("Внимание Возникла Ошибка!")
        print(repr(error))
        time.sleep(60)
