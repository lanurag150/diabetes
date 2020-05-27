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
       return render_template('index.php', prediction_text='<div class="col-lg-6" style="margin-top: 200px">
      <div class="w3-card-4" style="width:50%;">
    <header class="w3-container w3-black">
      <h1 style="color:white">Analysis Report</h1>
    </header>

    <div class="w3-container">
      <p id="result">You have been tested 'POSITIVE'</p>
    </div>

    <footer class="w3-container w3-black">
      <h5 style="color:white">Note :: All reports are made with 90% accuracy, please contact to our doctor.</h5>
    </footer>
  </div>
	</div>')
    else:
          return render_template('index.php', prediction_text='  <div class="col-lg-6" style="margin-top: 200px">
      <div class="w3-card-4" style="width:50%;">
    <header class="w3-container w3-black">
      <h1 style="color:white">Analysis Report</h1>
    </header>

    <div class="w3-container">
      <p id="result">You have been tested 'Negative'</p>
    </div>

    <footer class="w3-container w3-black">
      <h5 style="color:white">Note :: All reports are made with 90% accuracy, we're glad to inform you that you're safe.</h5>
    </footer>
  </div>
	</div>')  
if __name__ == "__main__":
    app.run(debug=True)
