# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:24:19 2016

@author: dheepan.ramanan
"""

import pandas as pd
import requests as rq
import json
import os

rootdir = '/Users/dheepan.ramanan/Documents/PintrestSuperbowl/pintrestScraper'

dfs = []
for paths,dirs, files in os.walk(rootdir):
	for filename in files:
		if filename.endswith(".json"):
			fullpath = os.path.join(rootdir,filename)
			df = pd.read_json(open(fullpath,'r'))
			df["topic"] = filename.split(".json")[0]
			df["ingredientsList"] = df["ingredientsList"].apply(lambda x: x.replace("\n",""))
			dfs.append(df)

	
	
superbowldata = pd.concat(dfs)
superbowl_uniques = superbowldata.drop_duplicates(subset = "description")
superbowl_uniques.to_excel('superbowlpins.xlsx')




			
			
 
