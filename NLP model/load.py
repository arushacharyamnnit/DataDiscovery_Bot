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

from spello.model import SpellCorrectionModel
sp = SpellCorrectionModel(language='en')
sp.load('SpellModel/model.pkl')

nlp = spacy.load('output/model-best')

ex = "give me job owner of joba"
# print(ex)
# ex=sp.spell_correct(ex)['spell_corrected_text']
print(ex)
doc = nlp(ex)

for ent in doc.ents:
    print(ent.text,ent.label_)