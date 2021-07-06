import elasticsearch
import os
import sys
from elasticsearch import Elasticsearch,helpers
import pandas as pd
import numpy as np
import json


df1=pd.read_csv('ocidw.csv',error_bad_lines=False)
df1.drop(columns=df1.columns[-1], 
        axis=1, 
        inplace=True)
df1.fillna("not defined", inplace=True)
    

df1=df1.to_dict('records')

es = Elasticsearch([{'host':'localhost','port':'9200'}])

# es.indices.delete(index="ocidw",ignore=[400,404])
es.indices.create(index="ocidw",ignore=400)


es = helpers.bulk(es,df1,index="ocidw")

