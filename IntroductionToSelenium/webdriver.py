from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True) #Web page stays open
driver = webdriver.Chrome(options = options)
driver.get(website)
driver.quit()
