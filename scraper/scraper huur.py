from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.common.exceptions

import smtplib

import pandas as pd
import numpy as np

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

#DRIVER_PATH = 'C:\\Users\\Luuk\\Downloads\\chromedriver_win32\\chromedriver.exe'
DRIVER_PATH = 'C:\\Users\\lschneid\\OneDrive - Centric\\Documents\\chromedriver\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://huurwoningen.nl/in/groningen')


#need:
#1: description: size, rooms, price, location
#2: link
#3: what website it is  for further comparison


#can turn these into classes, one overall class with all information as parent class

def huurwoningen(df):
    #number_of_listings = driver.find_element_by_xpath("/html/body/main/div[2]/form/div[1]/div/div[1]").get_attribute("innerHTML")
    #number_of_listings = str(number_of_listings)

    #number_listings_str = ''
    #for let in number_of_listings:
        #if let != ' ':
            #number_listings_str = number_listings_str + str(let)

    counter = 1
    while True:
        #elements on page go from first, 2-19, last
        #target = int(number_listings_str) #how to detract these from one another, so i can get listings last easily?

        #only adding new ones now. since older ones have a different structure: div[3] instead of div[4]

        try:
            if counter < 20:
                dict = {}
                dict["prijs"] = driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/span/div/span[1]').get_attribute("innerHTML")
                dict["grootte"] = driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/div[4]/dl/dd[1]/span[2]').get_attribute("innerHTML")
                dict["kamers"] = driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/div[4]/dl/dd[2]/span[2]').get_attribute("innerHTML")
                dict["locatie"] = driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/a/h2/span[2]/span[1]').get_attribute("innerHTML")
                dict["wijk"] = driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/div[1]').get_attribute("innerHTML")
                dict["link"] = driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/a').get_attribute("href")
                dict["source"] = driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/a').get_attribute("href").split('.nl')[0].split('//')[1]
                counter += 1
                df = df.append(dict, ignore_index = True)
                
            elif counter == 20:
                driver.find_element_by_xpath('//*[@id="pagination"]/ul/li[7]/a').click()
                counter = 1

        except selenium.common.exceptions.NoSuchElementException:
            break
        #except:
            #mail me
            #s = smtplib.SMTP("localhost")
            # https://docs.python.org/3/library/email.examples.html
            #additional 'except' which notifies me of issues with the specific website and error
    return df
    

        #alert me if new one is added
        #if one is removed have to remove it from df
        #update it to local csv file on raspberry pi, or whatever data it can hold and check this. how often refresh rate?


#driver.get('https://huurwoningen.nl/in/groningen') need to figure out if i can just reinstate this



def funda():
    while True:
        try:
            pass
        except selenium.common.exceptions.NoSuchElementException:
            pass
#websites to do: 
# funda, pararius, 123wonen, directwonen, kamernet
# evt nijstee?
#robots.txt voor: funda, pararius, directwonen, kamernet


column_names = ["prijs", "grootte", "kamers", "locatie", "wijk", "beschrijving", "link", "website"]

prijs = driver.find_element_by_xpath('//*[@id="listings"]/section[1]/section/div[1]/span/div/span[1]').get_attribute("innerHTML")
grootte = driver.find_element_by_xpath('//*[@id="listings"]/section[1]/section/div[1]/div[4]/dl/dd[1]/span[2]').get_attribute("innerHTML") 
kamers = driver.find_element_by_xpath('//*[@id="listings"]/section[1]/section/div[1]/div[4]/dl/dd[2]/span[2]').get_attribute("innerHTML") 
locatie = driver.find_element_by_xpath('//*[@id="listings"]/section[1]/section/div[1]/a/h2/span[2]/span[1]').get_attribute("innerHTML")  
wijk = driver.find_element_by_xpath('//*[@id="listings"]/section[1]/section/div[1]/div[1]').get_attribute("innerHTML") 
link = driver.find_element_by_xpath('//*[@id="listings"]/section[1]/section/div[1]/a').get_attribute("href")
source = driver.find_element_by_xpath('/html/head/link[7]').get_attribute("href").split('.nl')[0]

df_dict = {}

df_dict["prijs"] = ['placeholder']
df_dict["grootte"] = ['placeholder']
df_dict["kamers"] = ['placeholder']
df_dict["locatie"] = ['placeholder']
df_dict["wijk"] = ['placeholder']
df_dict["link"] = ['placeholder']
df_dict["source"] = ['placeholder']

df_dict["prijs"].append('placeholder2')
df_dict["grootte"].append('placeholder2')
df_dict["kamers"].append('placeholder2')
df_dict["locatie"].append('placeholder2')
df_dict["wijk"].append('placeholder2')
df_dict["link"].append('placeholder2')
df_dict["source"].append('placeholder2')

woningen_df = pd.DataFrame(df_dict)



#huurwoningen_df = huurwoningen(woningen_df)

#compare new items to those in db, so only those are added who are new
#delete items which are removed from the search query from the database
#remove the ones which are not on the websites, thus the native df


#when its up and running add date + time
#local database + app with flask. maybe export later


# can block some requests being made with selenium to speed up scraping:
    # https://www.scrapingbee.com/blog/selenium-python/ --> further down page

driver.quit()