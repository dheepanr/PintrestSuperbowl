# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:15:02 2016

@author: dheepan.ramanan
"""
import scrapy


class PintrestSpyder(scrapy.Spider):
	name = 'pintrest'
	allowed_domains =["pintrest.com"]
	start_urls =["http://www.pinterest.com/search/pins/?q=superbowl"]
	
	def parse(self, response):
		filename = response.url.split("/")[-2] + '.html'
		with open(filename, 'wb') as f:
			f.write(response.body)