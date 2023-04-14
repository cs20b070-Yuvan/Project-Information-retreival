from util import *

# Add your import statements here

from nltk.corpus import stopwords


class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = []

		#Fill in code here
		stopWords = set(stopwords.words("english"))
		for words in text: 
			removedWords = []
			removedWords = [word for word in words if not word in stopWords]
			stopwordRemovedText.append(removedWords)
			
		return stopwordRemovedText




	