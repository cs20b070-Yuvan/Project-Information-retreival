from sentenceSegmentation import SentenceSegmentation
from tokenization import Tokenization
from inflectionReduction import InflectionReduction
from stopwordRemoval import StopwordRemoval
from informationRetrieval import InformationRetrieval
from evaluation import Evaluation
from queryExpansion import QueryExpansion

from sys import version_info
import argparse
import json
import matplotlib.pyplot as plt

# Input compatibility for Python 2 and Python 3
if version_info.major == 3:
    pass
elif version_info.major == 2:
    try:
        input = raw_input
    except NameError:
        pass
else:
    print ("Unknown python version - input function not safe")

precision_list = []
recall_list = []
fscore_list = []
MAP_list = []
nDCG_list = []


class SearchEngine:

	def __init__(self, args):
		self.args = args
		# self.k = k

		self.tokenizer = Tokenization()
		self.sentenceSegmenter = SentenceSegmentation()
		self.inflectionReducer = InflectionReduction()
		self.stopwordRemover = StopwordRemoval()

		self.informationRetriever = InformationRetrieval()
		self.evaluator = Evaluation()
		self.queryExpansion = QueryExpansion()


	def segmentSentences(self, text):
		"""
		Call the required sentence segmenter
		"""
		if self.args.segmenter == "naive":
			return self.sentenceSegmenter.naive(text)
		elif self.args.segmenter == "punkt":
			return self.sentenceSegmenter.punkt(text)

	def tokenize(self, text):
		"""
		Call the required tokenizer
		"""
		if self.args.tokenizer == "naive":
			return self.tokenizer.naive(text)
		elif self.args.tokenizer == "ptb":
			return self.tokenizer.pennTreeBank(text)

	def reduceInflection(self, text):
		"""
		Call the required stemmer/lemmatizer
		"""
		return self.inflectionReducer.reduce(text)

	def removeStopwords(self, text):
		"""
		Call the required stopword remover
		"""
		return self.stopwordRemover.fromList(text)
	

	def preprocessQueries(self, queries):
		"""
		Preprocess the queries - segment, tokenize, stem/lemmatize and remove stopwords
		"""

		# Segment queries
		segmentedQueries = []
		for query in queries:
			segmentedQuery = self.segmentSentences(query)
			segmentedQueries.append(segmentedQuery)
		json.dump(segmentedQueries, open(self.args.out_folder + "segmented_queries.txt", 'w'))
		# Tokenize queries
		tokenizedQueries = []
		for query in segmentedQueries:
			tokenizedQuery = self.tokenize(query)
			tokenizedQueries.append(tokenizedQuery)
		json.dump(tokenizedQueries, open(self.args.out_folder + "tokenized_queries.txt", 'w'))
		# Stem/Lemmatize queries
		reducedQueries = []
		for query in tokenizedQueries:
			reducedQuery = self.reduceInflection(query)
			reducedQueries.append(reducedQuery)
		json.dump(reducedQueries, open(self.args.out_folder + "reduced_queries.txt", 'w'))
		# Remove stopwords from queries
		stopwordRemovedQueries = []
		for query in reducedQueries:
			stopwordRemovedQuery = self.removeStopwords(query)
			stopwordRemovedQueries.append(stopwordRemovedQuery)
		json.dump(stopwordRemovedQueries, open(self.args.out_folder + "stopword_removed_queries.txt", 'w'))

		preprocessedQueries = stopwordRemovedQueries
		return preprocessedQueries

	def expandQuery(self, processedQueries):
		if self.args.qexpander == 'yes':
			return self.queryExpansion.expansion(processedQueries)
		elif self.args.qexpander == 'no':
			return processedQueries
		else:
			exit('Sayonara')

	def preprocessDocs(self, docs):
		"""
		Preprocess the documents
		"""
		
		# Segment docs
		segmentedDocs = []
		for doc in docs:
			segmentedDoc = self.segmentSentences(doc)
			segmentedDocs.append(segmentedDoc)
		json.dump(segmentedDocs, open(self.args.out_folder + "segmented_docs.txt", 'w'))
		# Tokenize docs
		tokenizedDocs = []
		for doc in segmentedDocs:
			tokenizedDoc = self.tokenize(doc)
			tokenizedDocs.append(tokenizedDoc)
		json.dump(tokenizedDocs, open(self.args.out_folder + "tokenized_docs.txt", 'w'))
		# Stem/Lemmatize docs
		reducedDocs = []
		for doc in tokenizedDocs:
			reducedDoc = self.reduceInflection(doc)
			reducedDocs.append(reducedDoc)
		json.dump(reducedDocs, open(self.args.out_folder + "reduced_docs.txt", 'w'))
		# Remove stopwords from docs
		stopwordRemovedDocs = []
		for doc in reducedDocs:
			stopwordRemovedDoc = self.removeStopwords(doc)
			stopwordRemovedDocs.append(stopwordRemovedDoc)
		json.dump(stopwordRemovedDocs, open(self.args.out_folder + "stopword_removed_docs.txt", 'w'))

		preprocessedDocs = stopwordRemovedDocs
		return preprocessedDocs

	# def evaluateDataset2(self):
	# 	"""
	# 	- preprocesses the queries and documents, stores in output folder
	# 	- invokes the IR system
	# 	- evaluates precision, recall, fscore, nDCG and MAP 
	# 	  for all queries in the Cranfield dataset
	# 	- produces graphs of the evaluation metrics in the output folder
	# 	"""

	# 	# Read queries
	# 	queries_json = json.load(open(args.dataset + "cran_queries.json", 'r'))[:]
	# 	query_ids, queries = [item["query number"] for item in queries_json], \
	# 							[item["query"] for item in queries_json]
	# 	# Process queries 
	# 	processedQueries = self.preprocessQueries(queries)
  
	# 	# Query expansion
	# 	processedQueries = self.expandQuery(processedQueries)

	# 	# Read documents
	# 	docs_json = json.load(open(args.dataset + "cran_docs.json", 'r'))[:]
	# 	doc_ids, docs = [item["id"] for item in docs_json], \
	# 							[item["body"] + 2 * item["title"] for item in docs_json]
	# 	# Process documents
	# 	processedDocs = self.preprocessDocs(docs)

	# 	# Build document index
	# 	self.informationRetriever.buildIndex(processedDocs, doc_ids, self.args.dimred, self.args.ngrams, self.args.spellcheck)
	# 	# Rank the documents for each query
	# 	doc_IDs_ordered = self.informationRetriever.rank(processedQueries)

	# 	# Read relevance judements
	# 	qrels = json.load(open(args.dataset + "cran_qrels.json", 'r'))[:]

	# 	# Calculate precision, recall, f-score, MAP and nDCG for k = 1 to 10
	# 	eval_metrics =  []
	# 	precision = self.evaluator.meanPrecision(
	# 			doc_IDs_ordered, query_ids, qrels, 10)
	# 	eval_metrics.append(precision)
	# 	recall = self.evaluator.meanRecall(
	# 			doc_IDs_ordered, query_ids, qrels, 10)
	# 	eval_metrics.append(recall)
	# 	fscore = self.evaluator.meanFscore(
	# 			doc_IDs_ordered, query_ids, qrels, 10)
	# 	eval_metrics.append(fscore)
	# 	MAP = self.evaluator.meanAveragePrecision(
	# 			doc_IDs_ordered, query_ids, qrels, 10)
	# 	eval_metrics.append(MAP)
	# 	nDCG = self.evaluator.meanNDCG(
	# 			doc_IDs_ordered, query_ids, qrels, 10)
	# 	eval_metrics.append(nDCG)
	# 	self.evalmetrics = eval_metrics

	# 	# for k in range(1, 11):
	# 	# 	precision = self.evaluator.meanPrecision(
	# 	# 		doc_IDs_ordered, query_ids, qrels, k)
	# 	# 	if k == 10:
	# 	# 		precision_list.append(precision)
	# 	# 	precisions.append(precision)
	# 	# 	recall = self.evaluator.meanRecall(
	# 	# 		doc_IDs_ordered, query_ids, qrels, k)
	# 	# 	if k == 10:
	# 	# 		recall_list.append(recall)
	# 	# 	recalls.append(recall)
	# 	# 	fscore = self.evaluator.meanFscore(
	# 	# 		doc_IDs_ordered, query_ids, qrels, k)
	# 	# 	if k == 10:
	# 	# 		fscore_list.append(fscore)
	# 	# 	fscores.append(fscore)
	# 	# 	print("Precision, Recall and F-score @ " +  
	# 	# 		str(k) + " : " + str(precision) + ", " + str(recall) + 
	# 	# 		", " + str(fscore))
	# 	# 	MAP = self.evaluator.meanAveragePrecision(
	# 	# 		doc_IDs_ordered, query_ids, qrels, k)
	# 	# 	if k == 10:
	# 	# 		MAP_list.append(MAP)
	# 	# 	MAPs.append(MAP)
	# 	# 	nDCG = self.evaluator.meanNDCG(
	# 	# 		doc_IDs_ordered, query_ids, qrels, k)
	# 	# 	if k == 10:
	# 	# 		nDCG_list.append(nDCG)
	# 	# 	nDCGs.append(nDCG)
	# 	# 	print("MAP, nDCG @ " +  
	# 	# 		str(k) + " : " + str(MAP) + ", " + str(nDCG))



		# # Plot the metrics and save plot 
		# plt.plot(range(1, 11), precisions, label="Precision")
		# plt.plot(range(1, 11), recalls, label="Recall")
		# plt.plot(range(1, 11), fscores, label="F-Score")
		# plt.plot(range(1, 11), MAPs, label="MAP")
		# plt.plot(range(1, 11), nDCGs, label="nDCG")
		# plt.legend()
		# plt.title("Evaluation Metrics - Cranfield Dataset")
		# plt.xlabel("k")
		# plt.savefig(args.out_folder + "eval_plot.png")

	def evaluateDataset(self):
		"""
		- preprocesses the queries and documents, stores in output folder
		- invokes the IR system
		- evaluates precision, recall, fscore, nDCG and MAP 
		  for all queries in the Cranfield dataset
		- produces graphs of the evaluation metrics in the output folder
		"""

		# Read queries
		queries_json = json.load(open(args.dataset + "cran_queries.json", 'r'))[:]
		query_ids, queries = [item["query number"] for item in queries_json], \
								[item["query"] for item in queries_json]
		# Process queries 
		processedQueries = self.preprocessQueries(queries)
  
		# Query expansion
		processedQueries = self.expandQuery(processedQueries)

		# Read documents
		docs_json = json.load(open(args.dataset + "cran_docs.json", 'r'))[:]
		doc_ids, docs = [item["id"] for item in docs_json], \
								[item["body"] + 2 * item["title"] for item in docs_json]
		# Process documents
		processedDocs = self.preprocessDocs(docs)

		# Build document index
		self.informationRetriever.buildIndex(processedDocs, doc_ids, self.args.dimred, self.args.ngrams, self.args.spellcheck)
		# Rank the documents for each query
		doc_IDs_ordered = self.informationRetriever.rank(processedQueries)

		# Read relevance judements
		qrels = json.load(open(args.dataset + "cran_qrels.json", 'r'))[:]

		# Calculate precision, recall, f-score, MAP and nDCG for k = 1 to 10
		precisions, recalls, fscores, MAPs, nDCGs = [], [], [], [], []
		for k in range(1, 11):
			precision = self.evaluator.meanPrecision(
				doc_IDs_ordered, query_ids, qrels, k)
			if k == 10:
				precision_list.append(precision)
			precisions.append(precision)
			recall = self.evaluator.meanRecall(
				doc_IDs_ordered, query_ids, qrels, k)
			if k == 10:
				recall_list.append(recall)
			recalls.append(recall)
			fscore = self.evaluator.meanFscore(
				doc_IDs_ordered, query_ids, qrels, k)
			if k == 10:
				fscore_list.append(fscore)
			fscores.append(fscore)
			print("Precision, Recall and F-score @ " +  
				str(k) + " : " + str(precision) + ", " + str(recall) + 
				", " + str(fscore))
			MAP = self.evaluator.meanAveragePrecision(
				doc_IDs_ordered, query_ids, qrels, k)
			if k == 10:
				MAP_list.append(MAP)
			MAPs.append(MAP)
			nDCG = self.evaluator.meanNDCG(
				doc_IDs_ordered, query_ids, qrels, k)
			if k == 10:
				nDCG_list.append(nDCG)
			nDCGs.append(nDCG)
			print("MAP, nDCG @ " +  
				str(k) + " : " + str(MAP) + ", " + str(nDCG))

		# Plot the metrics and save plot 
		plt.plot(range(1, 11), precisions, label="Precision")
		plt.plot(range(1, 11), recalls, label="Recall")
		plt.plot(range(1, 11), fscores, label="F-Score")
		plt.plot(range(1, 11), MAPs, label="MAP")
		plt.plot(range(1, 11), nDCGs, label="nDCG")
		plt.legend()
		plt.title("Evaluation Metrics - Cranfield Dataset")
		plt.xlabel("k")
		plt.savefig(args.out_folder + "eval_plot.png")


	def handleCustomQuery(self):
		"""
		Take a custom query as input and return top five relevant documents
		"""

		#Get query
		print("Enter query below")
		query = input()
		# Process documents
		processedQuery = self.preprocessQueries([query])[0]
		processedQuery = self.expandQuery([processedQuery])[0]

		# Read documents
		docs_json = json.load(open(args.dataset + "cran_docs.json", 'r'))[:]
  
		if query[0:5] == 'body:':
			doc_ids, docs = [item["id"] for item in docs_json], \
							[item["body"] for item in docs_json]
		elif query[0:6] == 'title':
			doc_ids, docs = [item["id"] for item in docs_json], \
							[item["title"] for item in docs_json]
		elif query[0:7] == 'author':
			doc_ids, docs = [item["id"] for item in docs_json], \
							[item["author"] for item in docs_json]
		else:
			doc_ids, docs = [item["id"] for item in docs_json], \
							[item["body"] + 2 * item['title'] for item in docs_json]
		# Process documents
		processedDocs = self.preprocessDocs(docs)

		# Build document index
		self.informationRetriever.buildIndex(processedDocs, doc_ids, self.args.dimred, self.args.ngrams, self.args.spellcheck)
		# Rank the documents for the query
		doc_IDs_ordered = self.informationRetriever.rank([processedQuery])[0]

		# Print the IDs of first five documents
		print("\nTop five document IDs : ")
		for id_ in doc_IDs_ordered[:5]:
			print(id_)



if __name__ == "__main__":

	# Create an argument parser
	parser = argparse.ArgumentParser(description='main.py')

	# Tunable parameters as external arguments
	parser.add_argument('-dataset', default = "cranfield/", 
						help = "Path to the dataset folder")
	parser.add_argument('-out_folder', default = "output/", 
						help = "Path to output folder")
	parser.add_argument('-segmenter', default = "punkt",
	                    help = "Sentence Segmenter Type [naive|punkt]")
	parser.add_argument('-tokenizer',  default = "ptb",
	                    help = "Tokenizer Type [naive|ptb]")
	parser.add_argument('-custom', action = "store_true", 
						help = "Take custom query as input")
	parser.add_argument('-qexpander', default = "yes", 
						help = "Do query expansion [yes|no]")
	parser.add_argument('-dimred', default = "lsa", 
						help = "Do dimension reduction [lsa|no]")
	parser.add_argument('-ngrams', default = "u", 
						help = "Use ngrams [b|t|ub|bt|ubt]")
	parser.add_argument('-spellcheck', default = "yes",
						help = "Do spellcheck [yes|no]")
	parser.add_argument('-plots', default = "no",
		     			help = "Plot graphs [yes|no]")		     			
	
	# Parse the input arguments
	args = parser.parse_args()

	if args.plots == "yes":
		for k in range(100, 1500, 100):
			searchEngine = SearchEngine(args, k)
			precision_list.append(searchEngine.evalmetrics[0])
			recall_list.append(searchEngine.evalmetrics[1])
			fscore_list.append(searchEngine.evalmetrics[2])
			MAP_list.append(searchEngine.evalmetrics[3])
			nDCG_list.append(searchEngine.evalmetrics[4])
		plt.plot(range(100, 1500, 100), precision_list, label="Precision")
		plt.plot(range(100, 1500, 100), recall_list, label="Recall")
		plt.plot(range(100, 1500, 100), fscore_list, label="F-Score")
		plt.plot(range(100, 1500, 100), MAP_list, label="MAP")
		plt.plot(range(100, 1500, 100), nDCG_list, label="nDCG")
		plt.legend()
		plt.title("Evaluation Metrics at k = 10 - Cranfield Dataset")
		plt.xlabel("no. of dimensions")
		plt.savefig("plot.png")
	else:
		# Create an instance of the Search Engine
		searchEngine = SearchEngine(args)

	# Either handle query from user or evaluate on the complete dataset 
	if args.custom:
		searchEngine.handleCustomQuery()
	else:
		searchEngine.evaluateDataset()
