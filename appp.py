import pickle
from flask import Flask,render_template,request #flask 1 module, flask 2 class -->render-navigate to html file 
model=pickle.load(open('model.pkl','rb'))

app = Flask(__name__) #create the flask object

@app.route('/') # some open opens the server
def htmlPage():
    return render_template('index.html')

@app.route('/predict',methods=['post'])
def predict():
    # collecting data from form
    fd=float(request.form['fd'])
    result=model.predict([[fd]])
    return render_template('index.html', result=result)
    
    
if __name__=='__main__':
    app.run(host='127.0.0.1',port=5001,debug=True)