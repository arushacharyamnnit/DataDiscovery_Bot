from flask import Flask,render_template,redirect,url_for,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/get")
#function for the bot response
def get_bot_response():
    return f"hello"    

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
