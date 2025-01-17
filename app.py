import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.php')

@app.route('/predict',methods=['POST'])
def predict():
   
    int_features = [float(x) for x in request.form.values()]
 
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
   

    output = round(prediction[0], 2)
  
    if(output==1):
       return render_template('index.php', prediction_text='Test Is Positive')
    else:
          return render_template('index.php', prediction_text='Test Is Negative')  
if __name__ == "__main__":
    app.run(debug=True)
