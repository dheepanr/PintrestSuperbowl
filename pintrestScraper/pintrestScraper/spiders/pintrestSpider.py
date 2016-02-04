# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:15:02 2016

@author: dheepan.ramanan
"""
import scrapy
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
import time
import random
from pintrestScraper.items import PinterestscraperItem

class PintrestSpyder(scrapy.Spider):
	name = 'pintrest'
	allowed_domains =["pinterest.com"]
	start_urls =["https://www.pinterest.com/search/pins/?q=superbowl"]

	def parse(self, response):

		driver = webdriver.Chrome('/Users/dheepan.ramanan/anaconda/chromedriver/chromedriver')
		driver.get(response.url)
		time.sleep(5)
		
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)
		username = driver.find_element_by_id("userEmail")
		username.send_keys('kmz3p@virginia.edu')
		password = driver.find_element_by_id("userPassword")
		password.send_keys('11400clara')

		driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[3]/button/span').click()

		wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div[2]/div/div/div/div/div[2]')
		wrapper.find_element_by_id('userEmail').send_keys('kmz3p@virginia.edu')
		password2 = wrapper.find_element_by_id('userPassword')
		password2.send_keys('11400clara')
		password2.send_keys(Keys.RETURN)
		time.sleep(5)
				
		for i in range(1,30):
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(random.randint(1,3))

		body = bs(driver.page_source, 'html.parser')
		pinbodies = body.findAll('div',attrs={"class":"item  ui-draggable"})
		print "Count of Pins {}".format(len(pinbodies))
		for pin in pinbodies:
			pinurl = pin.find('div',attrs={'class':'pinHolder'}).find('a')['href']
			url = response.urljoin(pinurl)
			print url
			yield scrapy.Request(url, callback=self.parsePin)

		driver.quit()

	def parsePin(self, response):
			item = PinterestscraperItem()

			item["url"] = response.url

			pin = bs(response.body, 'html.parser')
			#Pin title
			try:
				item["title"] = pin.find('h2').text
			except AttributeError:
				item["title"] = 'Not Available'

			#Social stats
			try:
				item["repins"] = pin.find('div',attrs={"class":"repinCountContainer "}).find('p').text
				item["likes"] = pin.find('div',attrs={'class':"likeCountContainer "}).find('p').text
			except AttributeError:
				item["repins"] = ''
				item["likes"] =''

			#ingredients info
			try:
				ingredients = pin.find('h1',attrs={'class':'ingredientsTitle'})
				item["hasIngredients"] = 'True'
				item["ingredientsList"] = pin.find('div',attrs={'class':'pinDescriptionListTotal'}).text
			except AttributeError:
				item["hasIngredients"] = 'False'
				item["ingredientsList"] = ''

			#more info
			try:
				item["description"] = pin.find('div',attrs={"class":"pinDesc nonCanonicalDesc"}).text
			except AttributeError:
				item["description"]=''

			item["pinImage"] = pin.find('img',attrs={"class":"pinImage rounded"})['src']


			yield item







			