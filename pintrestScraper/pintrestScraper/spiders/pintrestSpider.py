# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:15:02 2016

@author: dheepan.ramanan
"""

import scrapy
from selenium import webdriver

class PintrestSpyder(scrapy.Spider):
	name = 'pintrest'
	allowed_domains =["pintrest.com"]
	start_urls =["https://www.pinterest.com/search/pins/?q=superbowl"]