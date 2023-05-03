# Add your import statements here

import numpy as np
from collections import defaultdict
from nltk.corpus import wordnet
from itertools import chain

# Add any utility functions here

# def buildVocab(docs):
#     words_synsets = []
#     unknown = 0
#     for doc in docs:
#         for sentence in doc:
#             for token in sentence:
#                 word = token.lower()
#                 if word.isalpha() == True: 
#                     synsets = wordnet.synsets(word)
#                     if len(synsets) > 0:
#                         words_synsets.append(synsets[0].name().split('.')[0])
#                     else:
#                         unknown += 1
#                         words_synsets.append(word)
#                 else:
#                     if '-' in word:
#                         synsets = wordnet.synsets(word)
#                         if len(synsets) > 0:
#                             words_synsets.append(synsets[0].name().split('.')[0])
#                         else:
#                             word1 = word.split('-')[0]
#                             word2 = word.split('-')[1]
#                             synsets1 = wordnet.synsets(word1)
#                             synsets2 = wordnet.synsets(word2)
#                             if len(synsets1) > 0:
#                                 words_synsets.append(synsets1[0].name().split('.')[0])
#                             else:
#                                 unknown += 1
#                                 words_synsets.append(word1)
#                             if len(synsets2) > 0:
#                                 words_synsets.append(synsets2[0].name().split('.')[0])
#                             else:
#                                 unknown += 1
#                                 words_synsets.append(word2)
#     return words_synsets

def expansion(collection):
    expand_collection = collection
    for i, col in enumerate(collection):
        for j, sentence in enumerate(col):
            expand_sentence = []
            for token in sentence:
                word = token.lower()
                if word.isalpha() == True:
                    synsets = wordnet.synsets(word)
                    if len(synsets) > 0:
                        expand_sentence.append(synsets[0].name().split('.')[0])
                    else:
                        expand_sentence.append(word)
                else:
                    if '-' in word:
                        synsets = wordnet.synsets(word)
                        if len(synsets) > 0:
                            expand_sentence.append(synsets[0].name().split('.')[0])
                        else:
                            word1 = word.split('-')[0]
                            word2 = word.split('-')[1]
                            synsets1 = wordnet.synsets(word1)
                            synsets2 = wordnet.synsets(word2)
                            if len(synsets1) > 0:
                                expand_sentence.append(synsets1[0].name().split('.')[0])
                            else:
                                expand_sentence.append(word)
                            if len(synsets2) > 0:
                                expand_sentence.append(synsets2[0].name().split('.')[0])
                            else:
                                expand_sentence.append(word)
            expand_collection[i][j] = sentence + expand_sentence
    expand_collection = [' '.join(list(chain.from_iterable(x))) for x in expand_collection]
    return expand_collection
            