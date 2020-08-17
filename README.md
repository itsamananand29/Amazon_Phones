# Amazon_Phones
# Amazon Product Scraper
This is an Amazon Product Scraper built using scapy module of python

# Features
it scrape the following things

Mobile Name
Mobile ImageLink
Mobile Price
Mobile Rating
Mobile Discount

By default it scrapes Mobile Phones from Amazon. In case you want to change it to scrape other product, follow the instructions

Open file phonescrape/spiders/amazon_spider.py
Chnage the urls list
Execute Amazon Scraper
you can execute the following command

scrapy crawl amazon -o phon.json
It will create phone.json file inside the phonescrape folder containing all the scraped data in JSON format.

# Sample Data
Already fetched sample data is available in phonescrape folder

# Preresuisites
Scrapy
Python 3.7

