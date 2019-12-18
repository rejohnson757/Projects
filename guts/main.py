from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.imdb.com/title/tt0944947/').text

soup = BeautifulSoup(source, 'html.parser')

artical = soup.find('artical')

title = soup.find('div', class_='title_wrapper')
summary = soup.find('div', class_='summary_text')
rating = soup.find('div', class_='ratingValue')
show_rating = soup.find('div', class_='subtext')
image = soup.find('div', class_='poster')

print(title.h1.text)
print('\n')
print(summary.text.strip())
print(rating.span.text)
print(show_rating.time.text.strip())
print(image.img)