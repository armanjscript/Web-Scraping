from selenium import webdriver
import pandas as pd

website = 'https://www.adamchoi.co.uk/overs/detailed'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True) #Web page stays open
driver = webdriver.Chrome(options = options)
driver.get(website)

all_matches_button = driver.find_element('xpath','//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements('tag name', 'tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element('xpath', './td[1]').text)
    home = match.find_element('xpath', './td[2]').text
    home_team.append(home)
    #print(home)
    score.append(match.find_element('xpath', './td[3]').text)
    away_team.append(match.find_element('xpath', './td[4]').text)

driver.quit()

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_data.csv', index = False)
print(df)