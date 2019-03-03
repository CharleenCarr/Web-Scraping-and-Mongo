import os
import time
import requests
import lxml.html
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser

def init_browser():
    executable_path = {'executable_path': 'C:/Users/CharCarr/Documents/Data_Science/02-Homework/12-Web-Scraping-and-Document-Databases/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
   
    mars_dict = {}

    nasa_url = ("https://mars.nasa.gov/news/")
    browser = init_browser()
    browser.visit(nasa_url)
    
    
    html = browser.html   
    # nasa_response = requests.get(nasa_url)
    nasa_soup = bs(html, "html.parser") 

    news_title = nasa_soup.find('div', class_ = 'content_title').text.strip()
    news_paragraph = nasa_soup.find('div', class_ = 'rollover_description_inner').text.strip()
    
    mars_dict["news_title"] = news_title
    mars_dict["news_paragraph"] = news_paragraph

# ---------------------------------------------------------------------
    
    nasa_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(nasa_image_url)

    html = browser.html
    nasa_image_soup = bs(html, 'html.parser')
    # print(nasa_image_soup.prettify())

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)

    browser.click_link_by_partial_text('more info')
    time.sleep(5)

    html = browser.html
    nasa_image_soup = bs(html, 'html.parser')
    # print(nasa_image_soup.prettify())

    browser.quit()

    featured_image_title = nasa_image_soup.find('h1', class_='article_title').text
    image_tags = nasa_image_soup.find('figure', class_='lede')

    link = image_tags.a['href']
    featured_image_url = 'https://www.jpl.nasa.gov' + link

    mars_dict["featured_image_title"] = featured_image_title.replace("\n", "").replace("\t", "").strip()
    mars_dict["featured_image_url"] = featured_image_url
    
# ----------------------------------------------------------------------

    twitter_url = ("https://twitter.com/marswxreport?lang=en")
    twitter_response = requests.get(twitter_url)
    twitter_soup = bs(twitter_response.text, "html.parser")

    mars_weather = twitter_soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    mars_dict["mars_weather"] = mars_weather[0].text

# -----------------------------------------------------------------------
    
    space_url = ("https://space-facts.com/mars/")
    html_table = pd.read_html(space_url)[0]
    mars_dict["space_table"] = dict(zip(html_table[0] , html_table[1]))
    
# ------------------------------------------------------------------------------------------------------------

    cerberus_hemisphere_url = ("https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced")
    cerberus_hemisphere_response = requests.get(cerberus_hemisphere_url)
    cerberus_hemisphere_soup = bs(cerberus_hemisphere_response.text, "html.parser")
       
    cerberus_hemisphere_title = cerberus_hemisphere_soup.find('h2', class_='title').text
    img_tags = cerberus_hemisphere_soup.find('div', class_='downloads')
    cerberus_hemisphere_image = img_tags.a['href']

    # cerberus_hemisphere_title, cerberus_hemisphere_image
    mars_dict["cerberus_hemisphere_title"] = cerberus_hemisphere_title
    mars_dict["cerberus_hemisphere_image"] = cerberus_hemisphere_image

# -------------------------------------------------------------------------------------------------------------

    schiaparelli_hemisphere_url = ("https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced")
    schiaparelli_hemisphere_response = requests.get(schiaparelli_hemisphere_url)
    schiaparelli_hemisphere_soup = bs(schiaparelli_hemisphere_response.text, 'html.parser')
    
    schiaparelli_hemisphere_title = schiaparelli_hemisphere_soup.find('h2', class_='title').text
    img_tags = schiaparelli_hemisphere_soup.find('div', class_='downloads')
    schiaparelli_hemisphere_image = img_tags.a['href']

#     # schiaparelli_hemisphere_title, schiaparelli_hemisphere_image
    mars_dict["schiaparelli_hemisphere_title"] = schiaparelli_hemisphere_title
    mars_dict["schiaparelli_hemisphere_image"] = schiaparelli_hemisphere_image

# -------------------------------------------------------------------------------------------------------------

    syrtis_major_hemisphere_url = ("https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced")
    syrtis_major_hemisphere_response = requests.get(syrtis_major_hemisphere_url)
    syrtis_major_hemisphere_soup = bs(syrtis_major_hemisphere_response.text, 'html.parser')
    
    syrtis_major_hemisphere_title = syrtis_major_hemisphere_soup.find('h2', class_='title').text
    img_tags = syrtis_major_hemisphere_soup.find('div', class_='downloads')
    syrtis_major_hemisphere_image = img_tags.a['href']

    # syrtis_major_hemisphere_title, syrtis_major_hemisphere_image
    mars_dict["syrtis_major_hemisphere_title"] = syrtis_major_hemisphere_title
    mars_dict["syrtis_major_hemisphere_image"] = syrtis_major_hemisphere_image

# -------------------------------------------------------------------------------------------------------------

    valles_marineris_hemisphere_url = ("https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced")
    valles_marineris_hemisphere_response = requests.get(valles_marineris_hemisphere_url)
    valles_marineris_hemisphere_soup = bs(valles_marineris_hemisphere_response.text, "html.parser")
    
    valles_marineris_hemisphere_title = valles_marineris_hemisphere_soup.find('h2', class_='title').text
    img_tags = valles_marineris_hemisphere_soup.find('div', class_='downloads')
    valles_marineris_hemisphere_image = img_tags.a['href']

    # valles_marineris_hemisphere_title, valles_marineris_hemisphere_image
    mars_dict["valles_marineris_hemisphere_title"] = valles_marineris_hemisphere_title
    mars_dict["valles_marineris_hemisphere_image"] = valles_marineris_hemisphere_image

    return mars_dict

# print(scrape())