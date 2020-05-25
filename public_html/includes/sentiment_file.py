#! C:/Users/DEll/AppData/Local/Programs/Python/Python38-32/python.exe

import sys
import os
import json
import matplotlib.pyplot as plt
import pandas as pd
from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect
import matplotlib.pyplot as plt
import numpy as np
import pickle
import math

def program_sentiment(hashtag):
	return json.dumps(hashtag + " hello you successfully executed python")

if __name__ == "__main__":
	def detector(x):
		try:
			return detect(x)
		except:
			None
	analyzer = SentimentIntensityAnalyzer()
	f = open("demo.txt", "w")
	start = str(sys.argv[3])
	f.write(sys.argv[1] + "\n")
	f.write(sys.argv[2] + "\n")
	f.write(start + "\n")
	start = start.replace('-', "")
	end = str(sys.argv[4])
	f.write(end)
	f.close()
	end = end.replace('-', "")
	format_str = '%Y%m%d'
	print(start)
	begin_date = dt.datetime.strptime(start, format_str)
	#print(begin_date)
	end_date = dt.datetime.strptime(end, format_str)
	

	limit = int(sys.argv[2])
	limit1 = math.ceil(limit * 1.3)
	lang = 'english'
	tweets = query_tweets(sys.argv[1], begindate = begin_date.date(), enddate = end_date.date(), limit = limit1, lang = lang)
	df = pd.DataFrame(t.__dict__ for t in tweets)

	df['lang'] = df['text'].apply(lambda x:detector(x))
	df = df[df['lang'] == 'en']

	sentiment = df['text'].apply(lambda x: analyzer.polarity_scores(x))

	df = pd.concat([df, sentiment.apply(pd.Series)], 1)
	df.drop_duplicates(subset = 'text', inplace = True)

	score = df['compound']
	

	np_hist = np.array(score)
	if len(np_hist) > int(limit):
		np_hist = np_hist[:int(limit)]
	hist,bin_edges = np.histogram(np_hist)
	print(bin_edges)

	plt.figure(figsize=[10,8])

	plt.bar(bin_edges[:-1], hist, width = 0.1,color='#0504aa',alpha=0.7)
	plt.xlim(min(bin_edges), max(bin_edges))
	plt.grid(axis='y', alpha=0.75)
	plt.xlabel('Compound Score',fontsize=15)
	plt.ylabel('Total Tweets',fontsize=15)
	plt.xticks(fontsize=15)
	plt.yticks(fontsize=15)
	plt.title('Sentimental Intensity Distribution ' + sys.argv[1] + ' for ' + str(len(np_hist)) + ' tweets',fontsize=15)
	plt.savefig('plot.png')
	print(program_sentiment(sys.argv[1]))
    
    







