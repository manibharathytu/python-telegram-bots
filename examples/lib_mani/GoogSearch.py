
import requests
from bs4 import BeautifulSoup
 
 
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
 
 
def fetch_results(search_term, number_results, language_code):
    assert isinstance(search_term, str), 'Search term must be a string'
    assert isinstance(number_results, int), 'Number of results must be an integer'
    escaped_search_term = search_term.replace(' ', '+')
 
    google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()
 
    return search_term, response.text

def search(search_term):
    
    keyword, html = fetch_results(search_term, 33, 'en')
    
    soup = BeautifulSoup(html, 'html.parser') #Page to soup
    srg=soup.select('div[class=g]')
    links_list=[]
    title_list=[]
    desc_list=[]
    for each in srg :
        
            link = each.find('a')
            
            href=link.get('href')
            if href is not None :
                if 'webcache' not in href :
                    if '#' not in href:
                        if 'search' not in href:
                            links_list.append(href)
                            title_list.append(link.getText())
                           # desc_list.append(span)
                            
                            
    return links_list,title_list

def get_links(search_term):
    ret=""
    links_list,title_list=search(search_term)
    for link in links_list:
        ret+=link+"\n"

    return ret
        
        


