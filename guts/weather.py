from bs4 import BeautifulSoup
import requests

source = requests.get('https://weather.com/weather/today/l/f892433d7660da170347398eb8e3d722d8d362fe7dd15af16ce88324e1b96e70').text
soup = BeautifulSoup(source, 'html.parser')

location = soup.find('div', class_='SocialMediaShareButton')
real_location = location.h1.text

temp = soup.find('div', class_='today_nowcard-temp')
real_temp = temp.span.text

describe = soup.find('div', class_='today_nowcard-phrase')
real_desribe = describe.text

print(real_location)
print(real_temp)
print(real_desribe)