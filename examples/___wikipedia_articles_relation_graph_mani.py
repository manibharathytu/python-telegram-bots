import urllib.request as ur
from bs4 import BeautifulSoup


wiki_url="https://en.wikipedia.org/wiki/" 
page_title="science"
url=wiki_url+page_title  #Url to be queried

page=ur.urlopen(url).read() # Get the page html

soup = BeautifulSoup(page, 'html.parser') #Page to soup

for link in soup.find_all('a'):
    href=link.get('href')
    
    if '#' not in href :        #To ignore in-page links for divs
        list.append(href)
    print(link)



 
 







