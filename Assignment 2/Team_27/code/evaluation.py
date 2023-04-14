from util import *

# Add your import statements here
import numpy as np
import statistics
from math import log

class Evaluation():

	def __init__(self):
		self.qrels = None

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		# Fill in code here

        # top K predicted document id's
		top_K_pred_docs = query_doc_IDs_ordered[:k]

		#number of relevant docs is the intersection of two sets 
		relevantdocs = len(set(top_K_pred_docs) & set(true_doc_IDs))
		precision = relevantdocs/k
		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here

		precisions = []
		 
		for i in range(len(query_ids)):
			relevant_docs = []
			for q_dict in qrels:
				if int(q_dict["query_num"]) == int(query_ids[i]) and int(q_dict["position"]) <= 4:
					relevant_docs.append(int(q_dict["id"]))

			doc_IDs_ordered_querywise = doc_IDs_ordered[i]

			individual_precision = self.queryPrecision(doc_IDs_ordered_querywise,query_ids[i],relevant_docs,k)

			precisions.append(individual_precision)

		meanPrecision = np.mean(precisions)

		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here
		top_K_pred_docs = query_doc_IDs_ordered[:k]
		# print(top_K_pred_docs)
		# print(true_doc_IDs)
		relevantdocs = len(set(top_K_pred_docs) & set(true_doc_IDs))
		totalrelevantdocs = len(true_doc_IDs)
		recall = relevantdocs/totalrelevantdocs
		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here

		recalls = []
		 

		for i in range(len(query_ids)):
			relevant_docs = []
			for q_dict in qrels:
				if int(q_dict["query_num"]) == int(query_ids[i]) and int(q_dict["position"]) <= 4:
					relevant_docs.append(int(q_dict["id"]))
				

			doc_IDs_ordered_querywise = doc_IDs_ordered[i]

			individual_recall = self.queryRecall(doc_IDs_ordered_querywise,query_ids[i],relevant_docs,k)

			recalls.append(individual_recall)

		meanRecall = np.mean(recalls)

		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here

		query_pre = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		query_rec = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		fscore = statistics.harmonic_mean([query_pre,query_rec])

		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here

		f1scores = []
		 

		for i in range(len(query_ids)):
			relevant_docs = []
			for q_dict in qrels:
				if int(q_dict["query_num"]) == int(query_ids[i]) and int(q_dict["position"]) <= 4:
					relevant_docs.append(int(q_dict["id"]))

			doc_IDs_ordered_querywise = doc_IDs_ordered[i]

			individual_f1 = self.queryFscore(doc_IDs_ordered_querywise,query_ids[i],relevant_docs,k)

			f1scores.append(individual_f1)

		meanFscore = np.mean(f1scores)

		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1
		qrels = self.qrels
		DCG = 0.0
		IDCG = 0.0
		
		relevancedict = {}
		for qdict in qrels:
			if query_id == int(qdict['query_num']):
				relevancedict[int(qdict['id'])] = (5 - int(qdict['position']))

		if len(relevancedict) < k:
			k = len(relevancedict)
		
		top_K_pred_docs = query_doc_IDs_ordered[:k]

		for i,docID in enumerate(top_K_pred_docs):
			if docID in relevancedict:
				DCG += (relevancedict[docID]/(log(i+1+1,2)))
			

		#DCG is computed

		#Now IDCG
		idealrank = list(relevancedict.values())
		#sort them in decreasing order
		idealrank.sort(reverse=True)
		ideal_K_pred_docs = idealrank[:k]
		for i,rel in enumerate(ideal_K_pred_docs):
			IDCG += (rel/(log(i+1+1,2)))
			
		if IDCG == 0:
			return 0
	
		nDCG = DCG/IDCG
		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here

		self.qrels = qrels
		nDCGs = []

		for i in range(len(query_ids)):
			nDCGs.append(self.queryNDCG(doc_IDs_ordered[i], query_ids[i], None, k))

		meanNDCG = np.mean(nDCGs)
		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here
		if len(query_doc_IDs_ordered) == 0 or k < 1:
			return -1
		
		k = min(k,len(query_doc_IDs_ordered))
		top_K_pred_docs = query_doc_IDs_ordered[:k]
		rel_doc_indices = [i for i in range(k) if top_K_pred_docs[i] in true_doc_IDs]
		if len(rel_doc_indices) == 0:
			return 0
		precisions = []
		for i in rel_doc_indices:
			individual_precision = self.queryPrecision(query_doc_IDs_ordered,query_id, true_doc_IDs,i+1)
			precisions.append(individual_precision)
		
		avgPrecision = np.sum(precisions)/len(precisions)
		return avgPrecision
		


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here
		avgprecisions = []

		for i in range(len(query_ids)):
			relevant_docs = []
			for q_dict in q_rels:
				if int(q_dict["query_num"]) == int(query_ids[i]) and int(q_dict["position"]) <= 4:
					relevant_docs.append(int(q_dict["id"]))

			doc_IDs_ordered_querywise = doc_IDs_ordered[i]

			individual_avgpre = self.queryAveragePrecision(doc_IDs_ordered_querywise,query_ids[i],relevant_docs,k)
			avgprecisions.append(individual_avgpre)

		meanAveragePrecision = np.mean(avgprecisions)

		return meanAveragePrecision

