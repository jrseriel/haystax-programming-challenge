import json
import collections
from datetime import date, timedelta

#Sample json
with open('mongodbexample.json', 'r') as handle:
	parsed = json.load(handle)

#Find most frequent word
def findmostfrequentword(parsed):
	fwlist = []
	for x in parsed:
		for y in x['words']:
			fwlist.append(y)
	mostfrequentword = (max(set(fwlist), key=fwlist.count))

	#Debug
	#print (mostfrequentword)
	return mostfrequentword

#Find most frequent word in last 24 hours(Since only a date is writted this is yesterday)
def findmostfrequentwordyesterday(parsed):
	today = (date.today())
	yesterday = (date.today()-timedelta(1))
	fwlist = []
	for x in parsed:
		if (str(x['date'])==str(yesterday)):
			for y in x['words']:
				fwlist.append(y)
	yesterdaymostfrequentword = (max(set(fwlist), key=fwlist.count))

	#Debug
	#print (yesterdaymostfrequentword)
	return yesterdaymostfrequentword

#Find the word trending the most(That is, the word that appears more today than it did yesterday)
def findtrendingword(parsed):
	today = (date.today())
	yesterday = (date.today()-timedelta(1))

	#Counter collection of today's words
	todaylist = []
	for x in parsed:
		if (str(x['date'])==str(today)):
			for y in x['words']:
				todaylist.append(y)
	todaycounter=collections.Counter(todaylist)
	#print (todaycounter)

	#Counter collection of yesterday's words
	yesterdaylist = []
	for x in parsed:
		if (str(x['date'])==str(yesterday)):
			for y in x['words']:
				yesterdaylist.append(y)
	yesterdaycounter=collections.Counter(yesterdaylist)
	#print (yesterdaycounter)

	#Compare the lists, subtract count differences
	for x in list(todaycounter):
		if (x not in yesterdaycounter):
			todaycounter.pop(x)
	for x in list(yesterdaycounter):
		if (x not in todaycounter):
			yesterdaycounter.pop(x)
	todaycounter.subtract(yesterdaycounter)
	#print (todaycounter)
	trendingword = max(todaycounter)

	#Debug
	#print (trendingword)
	return trendingword

#Call functions
print ("The most frequent word found in the documents is: "+findmostfrequentword(parsed));
print ("The most frequent word found in the documents with yesterday's date is: "+findmostfrequentwordyesterday(parsed));
print ("The trending word is: "+findtrendingword(parsed));