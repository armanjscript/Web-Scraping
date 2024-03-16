import requests
from bs4 import BeautifulSoup 

root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')

#pagination
pagination = soup.find('ul', class_='pagination')
pages = soup.find_all('li', class_='page-item')
last_page = pages[-2].text


for page in range(1, int(last_page)+1)[:2]: #just two pages
    result = requests.get(f'{website}?page={page}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    links = []

    for link in box.find_all('a', href=True):
        links.append(link['href'])


    for link in links:
        try:
            print(link)
            result = requests.get(f'{root}/{link}')
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
            box = soup.find('article', class_='main-article')
            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

            with open(f'{title}.txt', 'w', encoding='utf8') as file:
                file.write(transcript)
        except:
            print('---- Link not working ----')
        