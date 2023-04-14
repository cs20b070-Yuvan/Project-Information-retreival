from util import *

# Add your import statements here
import re
import nltk

class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None

		#Fill in code here
		"""Here we are using . ! ? as sentence enders"""
		delimiters = ".", "!", "?"
		regex_pattern = '|'.join('(?<={})'.format(re.escape(delim)) for delim in delimiters)
		segmentedText = re.split(regex_pattern,text)
		segmentedText = [i for i in segmentedText if i != ""]
		return segmentedText



	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		segmentedText = None

		#Fill in code here
		segmentedText = nltk.sent_tokenize(text)
		return segmentedText