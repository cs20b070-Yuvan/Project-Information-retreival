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



