import pandas as pd
import numpy as np
import json
from pathlib import Path
# Load NLP Pkgs
import spacy
#from wordcloud import WordCloud, STOPWORDS
from spacy.util import minibatch, compounding

import matplotlib.pyplot as plt
import re
import random
from spacy.tokens import DocBin
from tqdm import tqdm

nlp=spacy.load('en_core_web_sm')
# nlp = spacy.blank("en")

def load_data(file):
  with open(file,"r",encoding="utf-8") as f:
    data=json.load(f)
  return data





train= load_data("Training_Data/training_data_gloss.json")

def create_training(TRAIN_DATA):
  db = DocBin()
  for text,annot in TRAIN_DATA["annotations"]:
    text=text.lower()    
    # print(text,annot)    
    doc = nlp.make_doc(text)
    ents = []
    for start,end,label in annot["entities"]:
      span = doc.char_span(start,end,label=label,alignment_mode="contract")
      if span is None:
        print("skip")
      else:
        ents.append(span)
      doc.ents = ents
      db.add(doc)
  return (db)

train_data=create_training(train)
# test_data=create_training(test)
#print(train_data)
# train_data= 
train_data.to_disk("./data_gloss/train_data.spacy")
# test_data.to_disk("./data/test_data.spacy")


