from util import *

# imports 

class QueryExpansion():
    
    def expansion(self, collection):
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
        return expand_collection