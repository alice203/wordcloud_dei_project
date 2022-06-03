import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import matplotlib.pyplot as plt
import spacy
from textblob import TextBlob
from collections import Counter
import re

def get_character_name(string):
    new_string = string.str.lower().str.replace('_', ' ').str.split().str[1]
    return new_string

def clean_and_tokenize_description(df):
    d = (df
        .assign(desc_clean= lambda x: x['dev_en'].str.lower())
        )
    
    list_desc = list(d['desc_clean'])
    text_desc = ''.join(list_desc)
    td = re.sub(r'[^\w\s]','', text_desc)
    
    tm_tokens = word_tokenize(td)
    return tm_tokens

def extract_adjectives(text):
    blob = TextBlob(text)
    return [ word for (word,tag) in blob.tags if tag == "JJ"]


def get_df_gender(df, gender):
    df_new = (df
              .query(f"Gender == '" + gender + "'"))
    return df_new

def remove_stopwords(token_list):
    tm_tokens_without_sw = [word for word in token_list if not word in stopwords.words()]
    tm_without_sw = ' '.join(tm_tokens_without_sw)
    return tm_without_sw

def create_adjective_list(token_list):
    tm_without_sw = remove_stopwords(token_list)
    adjectives = extract_adjectives(tm_without_sw)
    adj_list = ' '.join(adjectives)
    return adj_list
                                     
def get_most_common_words(adjectives, number):
    # Adjective list
    adj_list = adjectives.split()
    # Count most common words
    counter =  Counter(adj_list)
    most_occur = counter.most_common(number)
    l = []
    for i in most_occur:
        l.append(i[0])
    return l

def create_removelist(m, f, n):
    remove_words = []
    for word in m: 
        if word in f:
            remove_words.append(word)
        if word in n:
            remove_words.append(word)
            
    rm = list(set(remove_words))
    rm2 = rm + ['new', 'little', 'big', 'many', 'dead', 'good', 'great', 'isnt', 'doesnt', 'dr', 'last', 
                'first', 'sure', 'magic', 'light', 'much', 'become',  'present', 'ready', 'true', 'first',
                'live', 'next', 'true', 'young', 'theyre', 'wish', 'future', 'protect', 'neobuki', 
                'samurai', 'key', 'spirit', 'born', 'tribe', 'youll',  'stole']
    
    return rm2

def remove_shared_adjectives(m_adj, f_adj, n_adj, remove_list):
    m_adjectives_wo_shared_words = [word for word in m_adj.split() if not word in remove_list]
    m_adj_wocw = ' '.join(m_adjectives_wo_shared_words)
    f_adjectives_wo_shared_words = [word for word in f_adj.split() if not word in remove_list]
    f_adj_wocw = ' '.join(f_adjectives_wo_shared_words)
    n_adjectives_wo_shared_words = [word for word in n_adj.split() if not word in remove_list]
    n_adj_wocw = ' '.join(n_adjectives_wo_shared_words)
    return m_adj_wocw, f_adj_wocw, n_adj_wocw