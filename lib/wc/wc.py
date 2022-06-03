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
    adj_list = ' '.join(m_adjectives)
    return adj_list
