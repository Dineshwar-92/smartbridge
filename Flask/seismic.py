from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)
lr=pickle.load(open('seismic.pkl','rb'))

@app.route('/')
def home():
    return render_template("seismic.html")


@app.route('/predict',methods=['post'])
def predict():
    Seismic=float(request.form['seismic'])
    Seismoacoustic=float(request.form['seismoacoustic'])
    Shift=float(request.form['shift'])
    Genergy=float(request.form['genergy'])
    Gpuls=float(request.form['gpuls'])
    Gdenergy=float(request.form['gdenergy'])
    Gdpuls=float(request.form['gdpuls'])
    Ghazard=float(request.form['ghazard'])
    Nbumps=float(request.form['nbumps'])
    Nbumps2=float(request.form['nbumps2'])
    Nbumps3=float(request.form['nbumps3'])
    Nbumps4=float(request.form['nbumps4'])
    Nbumps5=float(request.form['nbumps5'])
    Nbumps6=float(request.form['nbumps6'])
    Nbumps7=float(request.form['nbumps7'])
    Nbumps89=float(request.form['nbumps89'])
    Energy=float(request.form['energy'])
    Maxenergy=float(request.form['maxenergy'])
    
    a=np.array([[Seismic,Seismoacoustic,Shift,Genergy,Gpuls,Gdenergy,Gdpuls,Ghazard,Nbumps,Nbumps2,Nbumps3,Nbumps4,Nbumps5,Nbumps6,Nbumps7,Nbumps89,Energy,Maxenergy]])
    print(a)

    result=lr.predict(a)

    return render_template('seismic.html',x=result)

if __name__ == '__main__':
    app.run()