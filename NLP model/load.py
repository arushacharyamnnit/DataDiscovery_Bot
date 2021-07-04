import pandas as pd
from spacy.matcher import PhraseMatcher
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

nlp = spacy.load('output_ocidw/model-best')

while 1:
    print('Enter: ')
    ex=input()
    doc = nlp(ex)

    for ent in doc.ents:
        print(ent.text,ent.label_)