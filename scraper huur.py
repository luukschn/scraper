from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.common.exceptions

import smtplib

import pandas as pd
import numpy as np

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = 'C:\\Users\\Luuk\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://huurwoningen.nl/in/groningen')


#need:
#1: description: size, rooms, price, location
#2: link
#3: what website it is  for further comparison


#can turn these into classes, one overall class with all information as parent class

def huurwoningen(df):
    number_of_listings = driver.find_element_by_xpath("/html/body/main/div[2]/form/div[1]/div/div[1]").get_attribute("innerHTML")
    number_of_listings = str(number_of_listings)

    number_listings_str = ''
    for let in number_of_listings:
        if let != ' ':
            number_listings_str = number_listings_str + str(let)

    

    while True:
        counter = 1 #need to think about what results this will show properly
        #elements on page go from first, 2-19, last
        #target = int(number_listings_str) #how to detract these from one another, so i can get listings last easily?

        dict = {}
        
        dict["prijs"] = []
        dict["grootte"] = []
        dict["kamers"] = []
        dict["locatie"] = []
        dict["wijk"] = []
        dict["link"] = []
        dict["source"] = []

            # make a dict from the values

            # return df with dict values

            # (outside of function) append df with placeholder

        try:
            if counter < 20:    #first listing -- WORKS WITH NORMAL COUNTER AS WELL -- adjust to normal, not complete XPATH
                dict["prijs"].append(driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/span/div/span[1]').get_attribute("innerHTML"))
                dict["grootte"].append(driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/div[4]/dl/dd[1]/span[2]').get_attribute("innerHTML"))
                dict["kamers"].append(driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/div[4]/dl/dd[2]/span[2]').get_attribute("innerHTML"))
                dict["locatie"].append(driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/a/h2/span[2]/span[1]').get_attribute("innerHTML"))
                dict["wijk"].append(driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/div[1]').get_attribute("innerHTML"))
                dict["link"].append(driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/a').get_attribute("href"))
                dict["source"].append(driver.find_element_by_xpath(f'//*[@id="listings"]/section[{counter}]/section/div[1]/a').get_attribute("href").split('.nl')[0])
                output = df.append(dict, ignore_index = True)
            elif counter == 20:
                driver.find_element_by_xpath('//*[@id="pagination"]/ul/li[7]/a').click()
                counter = 1     #can also call it recursively?

        except selenium.common.exceptions.NoSuchElementException:
            print('except error')
            break
    return output
        #except:
            #mail me
            #s = smtplib.SMTP("localhost")
        #additional 'except' which notifies me of issues with the specific website and error
    

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

# prijs = driver.find_element_by_xpath('//*[@id="listings"]/section[1]/section/div[1]/span/div/span[1]').get_attribute("innerHTML")
# grootte = driver.find_element_by_xpath('//*[@id="listings"]/section[1]/section/div[1]/div[4]/dl/dd[1]/span[2]').get_attribute("innerHTML") 
# kamers = driver.find_element_by_xpath('//*[@id="listings"]/section[1]/section/div[1]/div[4]/dl/dd[2]/span[2]').get_attribute("innerHTML") 
# locatie = driver.find_element_by_xpath('//*[@id="listings"]/section[1]/section/div[1]/a/h2/span[2]/span[1]').get_attribute("innerHTML")  
# wijk = driver.find_element_by_xpath('//*[@id="listings"]/section[1]/section/div[1]/div[1]').get_attribute("innerHTML") 
# link = driver.find_element_by_xpath('//*[@id="listings"]/section[1]/section/div[1]/a').get_attribute("href")
# source = driver.find_element_by_xpath('/html/head/link[7]').get_attribute("href").split('.nl')[0]

df_dict = {}

df_dict["prijs"] = ['placeholder']
df_dict["grootte"] = ['placeholder']
df_dict["kamers"] = ['placeholder']
df_dict["locatie"] = ['placeholder']
df_dict["wijk"] = ['placeholder']
df_dict["link"] = ['placeholder']
df_dict["source"] = ['placeholder']

# df_dict["prijs"].append(prijs)
# df_dict["grootte"].append(grootte)
# df_dict["kamers"].append(kamers)
# df_dict["locatie"].append(locatie)
# df_dict["wijk"].append(wijk)
# df_dict["link"].append(link)
# df_dict["source"].append(source)

# df_dict2 = {}

# df_dict2["prijs"] = 'prijs'
# df_dict2["grootte"] = 'grootte'
# df_dict2["kamers"] = 'kamers'
# df_dict2["locatie"] ='locatie'
# df_dict2["wijk"] ='wijk'
# df_dict2["link"]= 'link'
# df_dict2["source"] = 'source'

woningen_df = pd.DataFrame(data=df_dict)

# output = df3.append(df_dict2, ignore_index=True)

print(huurwoningen(woningen_df))


##append everything to csv

#f = open("woningen.txt")
#lines = f.readlines()

#compare the dataframe to the csv of computer. append those which are not in it and send a notification
#remove the ones which are not on the websites, thus the native df

#pd.to_csv(woningen_df)

driver.quit()

