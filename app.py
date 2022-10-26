from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))
#victor=pickle.load(open('victor.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("analyse_sentiment.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    label = {0: 'negative', 1: 'positive'}
    entrée=[str(x) for x in request.form.values()]
    entrée_array=[np.array(entrée)]
    prediction=model.predict(entrée_array)
   
    if output>str(0.5):
        return render_template('analyse_sentiment.html',pred='le tweet est positif {}'.format(output))
        print ('hello')
    else:
        return render_template('analyse_sentiment.html',pred='le tweet est négatif {}'.format(output))
        print ('hello2')

if __name__ == '__main__':
    app.run()
