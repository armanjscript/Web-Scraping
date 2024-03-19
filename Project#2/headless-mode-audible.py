from selenium import webdriver
import pandas as pd

web = 'https://audible.com/search'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True) #Web page stays open
options.add_argument("--headless=new")
driver = webdriver.Chrome(options = options)
driver.get(web)
# driver.maximize_window()

container = driver.find_element('xpath', '//div[@class="adbl-impression-container "]')
titles = container.find_elements('xpath', ".//h3")
authors = container.find_elements('xpath', './/li[contains(@class, "authorLabel")]')
lengths = container.find_elements('xpath', './/li[contains(@class, "runtimeLabel")]')
book_title = []
book_author = []
book_length = []

for title in titles:
    book_title.append(title.text)

for author in authors:
    book_author.append(author.text)

for length in lengths:
    book_length.append(length.text)
    


driver.quit()


df_books = pd.DataFrame({'title':book_title, 'author':book_author, 'length':book_length})
df_books.to_csv('books_headless.csv', index = False)