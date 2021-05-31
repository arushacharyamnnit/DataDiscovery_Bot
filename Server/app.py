from __future__ import print_function

from flask import Flask,render_template,redirect,url_for,request
import pandas as pd
import numpy as np

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
from spacy.tokens import DocBin
nlp = spacy.load('../NLP model/output/model-best')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/user_input",methods=['POST'])
def get_user_response():
    user_input=request.form['msg']
    job={
        'JOB NAME':0,
        'JOB OWNER':0,
        'CONTACT TEAM':0,
        'CODEBASE LINK':0,
        'CONFLUENCE LINK':0
    }
    execution={
        'LAST RUN':0,
        'ACTIVE RUN':0,
        'NEXT RUN':0,
        'LAST RUN EXECUTION TIME':0,
    }
    print(user_input)
    doc = nlp(user_input)
    for ent in doc.ents:
        if ent.label_ in job:
            job[ent.label_]+=1
        if ent.label_ in execution:
            execution[ent.label_]+=1

    ans=DataUpdate(job,execution)        
    return (ans)



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
