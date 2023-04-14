from util import *

# Add your import statements here
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet

class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = []

		#Fill in code here
		porter = PorterStemmer()
		
		for words in text: 
			stemmedWords = []
			for word in words:
				stemmedWord = porter.stem(word)
				stemmedWords.append(stemmedWord)
			reducedText.append(stemmedWords)
		return reducedText


