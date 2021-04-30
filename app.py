from flask import Flask, render_template, request
import joblib
import numpy as np
app = Flask(__name__)

model = joblib.load('./forest_titanic.pkl')

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      sex = float(request.form.get('sex'))
      age = float(request.form.get('age'))
      sib = float(request.form.get('sib'))
      parch = float(request.form.get('parch'))
      pclass = float(request.form.get('pclass'))
      embark = request.form.get('embark')

      if pclass==1:
         Pclass_2 = 0
         Pclass_3 = 0
      elif pclass==2:
         Pclass_2 = 1
         Pclass_3 = 0
      elif pclass==3:
         Pclass_2 = 0
         Pclass_3 = 1         


      if embark =='S':
         Embarked_Q = 0
         Embarked_S = 1
      elif embark == 'Q':
         Embarked_Q = 1
         Embarked_S = 0
      elif embark == 'C':
         Embarked_Q = 0
         Embarked_S = 0


      a1 = [[sex, age, sib, parch, Pclass_2, Pclass_3, Embarked_Q, Embarked_S]]
      prediction = model.predict(a1)

      for i in range(0, len(prediction)):
         prediction[i] = round(int(prediction[i]))

      if prediction ==0:
         prediction = 'would not'
      else:
         prediction = 'would'

      return render_template('result.html', prediction = prediction)
app.run(debug = True)