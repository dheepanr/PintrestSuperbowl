# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:38:46 2016

@author: dheepan.ramanan
"""
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class JsDownload(object):


	def process_request(self, request, spider):
	    

	    driver = webdriver.PhantomJS(executable_path='/Users/dheepan.ramanan/Documents/Resources/phantomjs-2.1.1-macosx/bin/phantomjs')
	    driver.get(request.url)
	    time.sleep(5)
	    
	    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	    time.sleep(1)
	    username = driver.find_element_by_id("userEmail")
	    username.send_keys('kmz3p@virginia.edu')
	    password = driver.find_element_by_id("userPassword")
	    password.send_keys('11400clara')

	    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[3]/button/span').click()

	    wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div[2]/div/div/div/div/div[2]')
	    email = wrapper.find_element_by_id('userEmail').send_keys('kmz3p@virginia.edu')
	    password2 = wrapper.find_element_by_id('userPassword')
	    password2.send_keys('11400clara')
	    password2.send_keys(Keys.RETURN)
	    time.sleep(5)
				
	    for i in range(1,100):
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(random.randint(1,20))
				    
	    return HtmlResponse(request.url, encoding='utf-8', body=driver.page_source.encode('utf-8'))
	
	