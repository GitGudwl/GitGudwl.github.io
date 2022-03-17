
from selenium import webdriver
import urllib.request
import json
from datetime import datetime

PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(
    "https://www.metacritic.com/browse/games/score/metascore/all/all/filtered")

now = datetime.now()
gamelist = []
i = 1

for game in driver.find_elements_by_tag_name("tr"):
    print(game.text)
    for tag in game.find_elements_by_tag_name("a"):
        for img in tag.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))
            gamelist.append(
                {"Rating": game.text.split("\n")[0],
                 "No": game.text.split("\n")[1],
                 "Judul": game.text.split("\n")[2],
                 "platform": game.text.split("\n")[3],
                 "Release": game.text.split("\n")[4],
                 "waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S\n"),
                 "Image": img.get_attribute("src")
                 }
            )
hasil_scraping = open("hasilscraping.json", "w")
json.dump(gamelist, hasil_scraping, indent=5)
hasil_scraping.close()

driver.quit()
