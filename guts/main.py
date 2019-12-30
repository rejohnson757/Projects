from bs4 import BeautifulSoup
import requests

# web scraper

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

def search_tv():
    source_2 = requests.get('https://www.imdb.com/find?q=').text
    soup_2 = BeautifulSoup(source_2, 'html.parser')

    search = 'https://www.imdb.com/find?q='
    user_input = input('Please enter a TV show or Movie: ')
    user_search = search + user_input.replace(' ', '+')

    return user_search


    

link = search_tv()
source_3 = requests.get(link).text
soup_3 = BeautifulSoup(source_3, 'html.parser')
first_link = soup_3.find('td', class_='result_text').a['href']

#print(first_link)
imdb = 'https://imdb.com/' 
#print(imdb + first_link)

source_4 = requests.get(imdb + first_link).text

soup_4 = BeautifulSoup(source_4, 'html.parser')

article_2 = soup_4.find('article')


title_2 = soup_4.find('div', class_='title_wrapper')
summary_2 = soup_4.find('div', class_='summary_text')
rating_2 = soup_4.find('div', class_='ratingValue')
show_rating_2 = soup_4.find('div', class_='subtext')


	

print(title_2.h1.text)
print('\n')
print(summary_2.text.strip())
print(rating_2.span.text)
print(show_rating_2.time.text.strip())
