from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd

deals_url = 'https://store.steampowered.com/search/?specials=1&os=win'

#create connection, store content, close after retrieval.
request = uReq(deals_url)
raw_html = request.read()
request.close()

soup_html = soup(raw_html, "html.parser")
container = soup_html.find_all("div", {"class":"responsive_search_name_combined"})

titles = []
dates = []
ratings = []
prices = []

for game in container:
    if game.find("span", class_="title") is not None:
        #get title
        title = game.find("span", class_="title").text
        titles.append(title)

        #get date
        date = game.find("div", class_="col search_released responsive_secondrow").text
        dates.append(date)

        #get rating
        rating = game.find("div", class_="col search_discount responsive_secondrow").text
        #rating = game.find("div", class_="col search_reviewscore response_secondrow").text
        ratings.append(rating.strip().lstrip('-'))


        #get prices
        price = game.find("div", class_="col search_price discounted responsive_secondrow")
        the_price = price.strike.text
        prices.append(the_price)


test_df = pd.DataFrame({'Titles': titles,
                        'Dates': dates,
                        'Ratings': ratings,
                        'Price': prices})
print(test_df)













