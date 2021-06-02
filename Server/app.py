from __future__ import print_function

from flask import Flask,render_template,redirect,url_for,request,jsonify,json
import pandas as pd
import numpy as np
from collections import defaultdict
from pathlib import Path
# Load NLP Pkgs
import spacy
#from wordcloud import WordCloud, STOPWORDS
from spacy.util import minibatch, compounding

import sys
sys.path.insert(0, 'D:\DataDiscovery_Bot\DataDiscovery_Bot\Database')
from database_connectivity import DataUpdate
import matplotlib.pyplot as plt
import re
import random
from flask_mysqldb import MySQL,MySQLdb
from spacy.tokens import DocBin
nlp = spacy.load('../NLP model/output/model-best')
from spello.model import SpellCorrectionModel
sp = SpellCorrectionModel(language='en')
sp.load('../NLP model/SpellModel/model.pkl')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/user_input",methods=['POST'])
def get_user_response():
    user_input=request.form['msg']
    user_input=sp.spell_correct(user_input)['spell_corrected_text']
    job={
        'JID':1,
        'JOB_NAME':0,
        'JOB_OWNER':0,
        'CODEBASE_LINK':0,
         'CONFLUENCE_LINK':0,
        'CONTACT_TEAM':0,
    }
    execution={
        'JOB_NAME':0,
        'LAST_RUN':0,
        'ACTIVE_RUN':0,
        'NEXT_RUN':0,
        'LAST_RUN_EXECUTION_TIME':0,
    }

    # print(user_input)
    doc = nlp(user_input)
    for ent in doc.ents:
        # print(ent.label_)
        if ent.label_ in job:
            job[ent.label_]=ent.text
        if ent.label_ in execution:
            execution[ent.label_]=ent.text
           
    # print(job)
    ans=DataUpdate(job,execution) 
    return str(ans)











    
    # List=[]
    # Json={}
    
    
    # for result in ans:
    #     Json={ 'id':result[0], 'name':result[1],'email':result[2]}
    #     List.append(Json)
    #     Json={}
    # new_dict = {item['id']:item for item in List}
    # print(new_dict)
   



# @app.route("/get")
# #function for the bot response
# def get_bot_response():
#        return f"hello"  



# @app.route('/',methods=['POST','GET'])    
# def login():
#     if request.method=='POST':
#         user=request.form['data']
#         return redirect(url_for('user',usr=user))
#     else:
#         return render_template('index.html')    

# @app.route("/<usr>")
# def user(usr):
#     return f"<h1>{usr}</h1>"

if __name__=="__main__":
    app.run(debug=True,port=8000)    
