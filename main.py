import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

file = open("games.csv", "w", encoding="utf-8")
write_obj = csv.writer(file)
write_obj.writerow(["Game", "Cover Image"])

ind = 1

from random import randint
while ind < 6:
    url = f'https://store.playstation.com/en-us/pages/browse/{ind}'
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    game_list = soup.find('ul', class_='psw-grid-list psw-l-grid')
    all_games = game_list.find_all('li', class_="psw-l-w-1/2@mobile-s psw-l-w-1/2@mobile-l psw-l-w-1/6@tablet-l psw-l-w-1/4@tablet-s psw-l-w-1/6@laptop psw-l-w-1/8@desktop psw-l-w-1/8@max")

    for game in all_games:
        images = game.find_all('img')
        img_address = images[1]['src']  ## ერთზე მეტი სურათის ლინკია კოდში, ეს მეორეს, უფრო მაღალ ხარისხიანს ინახავს
        print(img_address)

        title_section = game.find('section', class_="psw-product-tile__details psw-m-t-2")
        title = title_section.find('span', class_="psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2").text
        print(title)

        write_obj.writerow([title, img_address])

    sleep(randint(1, 4))
    ind += 1

file.close()