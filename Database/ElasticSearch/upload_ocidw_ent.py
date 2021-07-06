import elasticsearch
import os
import sys
from elasticsearch import Elasticsearch,helpers
import pandas as pd
import numpy as np
import json


df2=pd.read_csv('ocidw1.csv',error_bad_lines=False)
df2.fillna("not defined", inplace=True)

df2=df2.to_dict('records')



es = Elasticsearch([{'host':'localhost','port':'9200'}])

# es.indices.delete(index="ocidw_ent",ignore=[400,404])

es.indices.create(index="ocidw_ent",ignore=400)

es = helpers.bulk(es,df2,index="ocidw_ent")

