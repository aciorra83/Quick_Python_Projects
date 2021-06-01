# Importing necessary libraries
import requests
# selecting only BeautifulSoup from bs4 library
from bs4 import BeautifulSoup as bs

github_user = input('Enter github username: ')
url = 'https://github.com/' + github_user
# sends a request to the user input url
r = requests.get(url)
# soup now is the html content of the url
soup = bs(r.content, 'html.parser')

# specifying html tags for the program to search for
profile_img = soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_img)
