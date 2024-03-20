from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

web = 'https://www.audible.com/adblbestsellers?ref_pageloadid=not_applicable&ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=334a4a9c-12d2-4c3f-aee6-ae0cbc6a1eb0&pf_rd_r=7MVY88Z48MBGWSECXDAY&pageLoadId=wb82o4POBeuwxJIw&creativeId=7ba42fdf-1145-4990-b754-d2de428ba482'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True) #Web page stays open
driver = webdriver.Chrome(options = options)
driver.get(web)
driver.maximize_window()


#Pagination
pagination = driver.find_element('xpath', '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements('tag name', 'li')
last_page = int(pages[-2].text)

book_title = []
book_author = []
book_length = []


current_page = 1
while current_page <= last_page:
    time.sleep(2)
    container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="adbl-impression-container "]')))
    #container = driver.find_element('xpath', '//div[@class="adbl-impression-container "]')
    titles = container.find_elements('xpath', ".//h3")
    authors = container.find_elements('xpath', './/li[contains(@class, "authorLabel")]')
    lengths = container.find_elements('xpath', './/li[contains(@class, "runtimeLabel")]')
    
    for title in titles:
        book_title.append(title.text)

    for author in authors:
        book_author.append(author.text)

    for length in lengths:
        book_length.append(length.text)
    
    current_page = current_page + 1
    try:
        next_page = driver.find_element('xpath', '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass
    

driver.quit()


df_books = pd.DataFrame({'title':book_title, 'author':book_author, 'length':book_length})
df_books.to_csv('books_pagination_waits.csv', index = False)