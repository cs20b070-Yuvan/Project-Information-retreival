# from nltk.corpus import wordnet
# from collections import Counter

# def expand_query(query, k):
#     # Tokenize the query into a list of words
#     words = query.split()
#     expanded_query = []
    
#     # Iterate over each word in the query
#     for word in words:
#         # Get the k most frequently used synsets for the word
#         synsets = wordnet.synsets(word)
#         synset_counts = Counter([synset for s in synsets for synset in s.lemmas()])
#         most_frequent_synsets = [synset for synset, count in synset_counts.most_common(k)]
        
#         # Combine the original word with the most frequent synonyms
#         expanded_query.append(word)

#         if not most_frequent_synsets:
#             continue
#         expanded_query.append(word)
#         expanded_word = " ".join([most_frequent_synsets[0].name()] + [synset.name().split('.')[0] for synset in most_frequent_synsets[1:]])
#         expanded_query.append(expanded_word)
    
#     # Combine the expanded words into a single query
#     return " ".join(expanded_query)


# # Example usage
# query = "what similarity laws must be obeyed when constructing aeroelastic models"
# k = 2
# expanded_query = expand_query(query, k)
# print(expanded_query)


import matplotlib.pyplot as plt

precision_list = [ 0.33111111111111113, 0.34, 0.33244444444444443, 0.3297777777777777, 0.32755555555555554, 0.3235555555555556, 0.32222222222222224 , 0.3182222222222222, 0.3142222222222222,  0.31199999999999994, 0.312, 0.31333333333333335, 0.3124444444444444,0.31155555555555553]
recall_list = [0.47339650146486556, 0.4918595494182341,  0.48507038749169284, 0.47579009247806436, 0.4747453326856266, 0.466728698897063 , 0.46651207420004615 , 0.4625513643445995, 0.4587850855979286, 0.4542341753607438, 0.4531648496247514, 0.4558601173200191, 0.455500547065712 , 0.4547226804027879 ]
fscore_list = [0.36192331429690666, 0.3724650314968483,0.36554969552843225,0.36093535007054633,0.3589933189878591,0.35384224371704365, 0.352983076164928 ,0.34915936274364867, 0.3453832741601956, 0.34243390459700335, 0.3420152056757872, 0.34376665695720665, 0.34308756992403194 ,0.34234472822466855]
MAP_list = [0.6695774985302763, 0.6976444962347078, 0.7126303364967386, 0.7156617493911145, 0.7210062505249013, 0.7150133030990174 , 0.7125222474174855 , 0.7072057634164777, 0.7046784594496234, 0.7051038695725202, 0.6989332556479382, 0.6946684912236499, 0.6935388783908625 , 0.6910115184345343 ]
nDCG_list = [0.4812901735735382, 0.4969990860178917, 0.5019879598950918, 0.5031414302454987, 0.5041609631116184, 0.4955417912003149 , 0.49431462235823836 , 0.48655000426831124, 0.48573774185490254, 0.4836945438076645, 0.482136841166389, 0.48063025609779425, 0.4790146848237778 , 0.4777498736767271 ]

plt.plot(range(100, 1500, 100), precision_list, label="Precision")
plt.plot(range(100, 1500, 100), recall_list, label="Recall")
plt.plot(range(100, 1500, 100), fscore_list, label="F-Score")
plt.plot(range(100, 1500, 100), MAP_list, label="MAP")
plt.plot(range(100, 1500, 100), nDCG_list, label="nDCG")
plt.legend()
plt.title("Evaluation Metrics at k = 10 - Cranfield Dataset")
plt.xlabel("no. of dimensions")
plt.savefig("plot.png")