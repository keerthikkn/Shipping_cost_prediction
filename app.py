import pickle
import pandas as pd
import numpy as np
from flask import Flask,request,app,jsonify,url_for,render_template

app=Flask(__name__)
#loading the model
model = pickle.load(open('lr_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods = ['post'])
def predict_api():
    data = request.json['data']
    print(data)
    data = np.array(list(data.values())).reshape(1,-1)
    output = model.predict(data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    data =np.array(data).reshape(1,-1)
    print(data)
    output=model.predict(data)[0]
    return render_template("home.html",prediction_text="Estimated shipping cost is {}".format(output))


if __name__=="__main__":
    app.run(debug=True)

