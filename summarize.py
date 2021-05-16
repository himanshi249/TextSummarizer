#import all libraries
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

print("Hello world")

def read_article(text_clean):
    article=text_clean.split(".")
    sentences=[]  

    for sentence in article: 
        print(sentence)
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" ")) #period at the end of sentences are replaces by space
    sentences.pop()
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords=[]
    
    sent1=[w.lower() for w in sent1]
    sent2=[w.lower() for w in sent2]

    all_words= list(set(sent1+sent2))

    vector1= [0] * len(all_words)
    vector2=[0]*len(all_words)

    #build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] +=1 

    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] +=1 
    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
    #Create an empty similarity matrix   
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1==idx2: #ignore if both are same sentences
                continue
            similarity_matrix[idx1][idx2]=sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix

def generate_summary(text_clean, top_n=5):
    stop_words= stopwords.words('english')
    summarize_text=[]

    #1. Read text and split it
    
    sentences= read_article(text_clean)

    #2. Generate Similarity Matrix across sentences 
    sentence_similarity_matrix= build_similarity_matrix(sentences, stop_words)

    #3. Rank sentences in similarity matrix
    sentence_similarity_graph=nx.from_numpy_array(sentence_similarity_matrix) 
    scores= nx.pagerank_numpy(sentence_similarity_graph) #,  max_iter=6000
   

    #4. Sort the rank and pick top sentences 
    ranked_sentence= sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
    print("Indexes of top ranked_sentence order are ", ranked_sentence)

    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))
    
    print("Summary:".join(summarize_text))
    return summarize_text
    
    
