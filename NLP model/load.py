import pandas as pd
import numpy as np

from pathlib import Path
# Load NLP Pkgs
import spacy
#from wordcloud import WordCloud, STOPWORDS
from spacy.util import minibatch, compounding

import matplotlib.pyplot as plt
import re
import random
from spacy.tokens import DocBin

nlp = spacy.load('output/model-best')

ex = "what is codebase link and last run of C"

doc = nlp(ex)

for ent in doc.ents:
    print(ent.text,ent.label_)