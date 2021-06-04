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


re = load_data("train_data.json")

# print(re)
train=re


def create_training(TRAIN_DATA):
  db = DocBin()
  for text,annot in tqdm(TRAIN_DATA["annotations"]):
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

#print(train_data)
# train_data= 
train_data.to_disk("./data/train_data.spacy")
