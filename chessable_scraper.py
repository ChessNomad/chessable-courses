#Thanks to herinoantony for this great example
# --> https://github.com/henrionantony/Dynamic-Web-Scraping-using-Python-and-Selenium/blob/master/indeed.py

from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
import pandas as pd
from random import randint
import numpy as np

website = """
#########################################
#         WEBSITE: Chessable.com        #
######################################### 
"""
print(website)
start_time = datetime.now()
print('Crawl starting time : {}' .format(start_time.time()))
print()

course_link = []
course_title = []
course_type = []
author = []
price = []
price_with_video = []
course_rating = []
course_rating_count = []

rubies = []

target_color = []
beginning = []
casual = []
intermediate = []
advanced = []
expert = []
language = []
instruction_word_count = []
free_video = []
trainable_variations = []
avg_line_depth = []
released_on = []
support_level = []
section = []

#The page has 19 pages, I have checked that beforehand.
for i in range(1,20):

    print("Building webdriver")
    driver = webdriver.Chrome('C:\\Users\\Superbeckenbauer\\chromedriver_win32\\chromedriver.exe')
    
    
    if i == 1:
        url = 'http://chessable.com/courses'
    else:
        url = 'https://www.chessable.com/courses/?page={}'.format(str(i))
    
    driver.get(url)
    time.sleep(randint(1,3))
    
    cards = driver.find_elements(By.XPATH, '//a[@class="book-card__link"]')
    card_links = []
    for card in cards:
        card_links.append(card.get_attribute('href'))
        
    for link in card_links:
        #surfing to the link
        driver.get(link)
        print("surfed to: {}".format(driver.current_url))
        time.sleep(randint(1,2))
        
        #Collecting the link
        course_link.append(driver.current_url)
        
        #Collecting the course title
        course_title.append(driver.find_element(By.XPATH, '//h1[@class="book-cover__title book-cover__title--desktop"]').text)
        
        #getting the subtitle text
        type_author = driver.find_element(By.XPATH, '//span[@class="book-cover__author"]').text
        
        #collecting the author and course type from the subtitle text
        course_type.append(type_author.split(' by ')[0])
        author.append(type_author.split(' by ')[1])
        
        #The price is tricky because there ar many possible elements. 
        #This is the price attribute, if there is no price it is obviously free. 
        #Otherwise we check for an extra element called price_with_video.
        if not driver.find_elements(By.XPATH, '//span[@data-price]'):
            price.append(0)
            price_with_video.append(np.nan)
        else:
            if len(driver.find_elements(By.XPATH, '//span[@data-price]')) > 1:
                price.append(driver.find_elements(By.XPATH, '//span[@data-price]')[0].text)
                price_with_video.append(driver.find_elements(By.XPATH, '//span[@data-price]')[1].text)
            else:
                price.append(driver.find_element(By.XPATH, '//span[@data-price]').text)
                price_with_video.append(np.nan)
        
        #Ratings might or might not be there. 
        if not driver.find_elements(By.XPATH, '//span[@itemprop="ratingValue"]'):
            course_rating.append(np.nan)
        else:
            course_rating.append(driver.find_element(By.XPATH, '//span[@itemprop="ratingValue"]').text)
        
        #Same goes for the collection of rating count
        if not driver.find_elements(By.XPATH, '//span[@itemprop="ratingCount"]'):
            course_rating_count.append(np.nan)
        else:
            course_rating_count.append(driver.find_element(By.XPATH, '//span[@itemprop="ratingCount"]').text)
        
        #Collecting rubies BLING BLING
        if not driver.find_elements(By.XPATH, '//*[@id="bookRuby"]'):
            rubies.append(0)
        else:
            rubies.append(driver.find_element(By.XPATH, '//*[@id="bookRuby"]').text)
        
        #Right now all other elements are so called 'infobits.' They all have the same class.
        #Therefore it is best to try and process them all at the same time!
        infobits = driver.find_elements(By.XPATH, '//*[@class="infoBit"]')
        
        #This is a list of lists, to order the elements
        clean_infobits = []
        for bit in infobits:
            clean_infobits.append(bit.text.split('\n'))
        
        #We can filter the clean infobits list on its first element. Collecting the color here.
        fr = list(filter(lambda x: x[0] == 'For:', clean_infobits))
        if not fr:
            target_color.append(np.nan)
        else:
            target_color.append(fr[0][1])
                
        #This big pile of if if statements finds out for which level the courses are meant.
        lvl = list(filter(lambda x: x[0] == 'Recommended for:', clean_infobits))
        if not lvl:
            beginning.append(np.nan)
            casual.append(np.nan)
            intermediate.append(np.nan)
            advanced.append(np.nan)
            expert.append(np.nan) 
        else:
            level_list = lvl[0][1:]
            if not any('Beginning' in c for c in level_list):
                beginning.append(0)
            else:
                beginning.append(1)

            if not any('Casual' in c for c in level_list):
                casual.append(0)
            else:
                casual.append(1)

            if not any('Intermediate' in c for c in level_list):
                intermediate.append(0)
            else:
                intermediate.append(1)

            if not any('Advanced' in c for c in level_list):
                advanced.append(0)
            else:
                advanced.append(1)

            if not any('Expert' in c for c in level_list):
                expert.append(0)
            else:
                expert.append(1)
        
        #Collecting the language
        lan = list(filter(lambda x: x[0] == 'Language:', clean_infobits))
        if not lan:
            language.append(np.nan)
        else:
            language.append(lan[0][1])
        
        #Collecting instruction_word_count
        ins = list(filter(lambda x: x[0] == 'Instruction:', clean_infobits))
        if not ins:
            instruction_word_count.append(np.nan)
        else:
            instruction_word_count.append(ins[0][1].split(' ')[0])

        #Collecting free_video
        frv = list(filter(lambda x: x[0] == 'Free video:', clean_infobits))
        if not frv:
            free_video.append(np.nan)
        else:
            free_video.append(frv[0][1])

        #Collecting trainable_variations
        #For the other variables it is the same function
        trv = list(filter(lambda x: x[0] == 'Trainable variations:', clean_infobits))
        if not trv:
            trainable_variations.append(np.nan)
        else:
            trainable_variations.append(trv[0][1])
         
        ald = list(filter(lambda x: x[0] == 'Avg. line depth:', clean_infobits))
        if not ald:
            avg_line_depth.append(np.nan)
        else:
            avg_line_depth.append(ald[0][1])
            
        relo = list(filter(lambda x: x[0] == 'Released on:', clean_infobits))
        if not relo:
            released_on.append(np.nan)
        else:
            released_on.append(relo[0][1])

        slvl = list(filter(lambda x: x[0] == 'Support level:', clean_infobits))
        if not slvl:
            support_level.append(np.nan)
        else:
            support_level.append(slvl[0][1])
            
        sec = list(filter(lambda x: x[0] == 'Section:', clean_infobits))
        if not sec:
            section.append(np.nan)
        else:
            section.append(sec[0][1])
                
    print('Crawling status for "{}" : Done' .format(url))
    print()
        
    driver.quit()
    print('Crawling time : {}' .format(datetime.now() - start_time))



#In order to debug.
print(len(course_link),len(course_title),len(course_type),len(author), len(price), len(price_with_video), len(course_rating), len(course_rating_count), len(rubies), len(target_color), len(beginning), len(casual), len(intermediate), len(advanced), len(expert), len(language), len(instruction_word_count),len(free_video),len(trainable_variations), len(avg_line_depth), len(released_on), len(support_level), len(section))

# Dataframe creation
df = pd.DataFrame({
    'course_link': course_link,
    'course_title': course_title,
    'course_type': course_type,
    'author': author, 
    'price': price,
    'price_with_video': price_with_video,
    'course_rating': course_rating,
    'course_rating_count': course_rating_count,
    'rubies': rubies,
    'target_color': target_color,
    'beginning': beginning,
    'casual': casual,
    'intermediate': intermediate,
    'advanced': advanced,
    'expert': expert,
    'language': language,
    'instruction_word_count': instruction_word_count,
    'free_video': free_video,
    'trainable_variations': trainable_variations,
    'avg_line_depth': avg_line_depth,
    'released_on': released_on,
    'support_level': support_level,
    'section': section
})

csv_file = 'chessable_data_30072020.csv'
df.to_csv(csv_file)

print('Dataframe successfuly created and exported')