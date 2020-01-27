import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
   
    int_features = [float(x) for x in request.form.values()]
    print(int_features)
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    print(prediction)
   

    output = round(prediction[0], 2)
    print(output)
    if(output==1):
      return render_template('index.html', prediction_text='RESULT IS POSITIVE')
    else:
          return render_template('index.html', prediction_text='RESULT IS NEGATIVE')
if __name__ == "__main__":
    app.run(debug=False)
