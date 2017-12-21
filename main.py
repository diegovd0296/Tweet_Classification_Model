#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:48:33 2017

@author: diego
"""

import os

import runtime_parser as rp
import handler
import classifier
import crawler


def main():

	print '\n'

	if not os.path.exists(rp.target):
		os.makedirs(rp.target)


	table,positives,negatives,p_tweets,n_tweets = handler.load_table("table/table.csv")
	filename = rp.target + "/tweets.csv"

	#Scrap Tweets and store them in csv file
	crawler.go_spider_go(filename,rp.target,retweets=rp.rt,scroll_pause=float(rp.sp),headless=rp.headless)

	tweets = handler.load_tweets(rp.target +"/tweets.csv")

	positive_ratio,group = classifier.classify(tweets,table,positives,negatives,p_tweets,n_tweets)

	tag = 'user' if '@' in rp.target else 'hashtag'

	print "%s is a  %s %s" % (rp.target,group.lower(),tag) 
	print "Positive Ratio: %.2f\n" % positive_ratio


if __name__ == "__main__":
	main()	