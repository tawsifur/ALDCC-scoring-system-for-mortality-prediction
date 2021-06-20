# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 00:54:16 2021

@author: LEGION
"""

  
# Importing essential libraries

from flask import Flask, render_template, request
import pickle
import numpy as np
import math



app = Flask(__name__) 

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Age=int(request.form['Age'])
        Lymphocyte_Count=float(request.form['Lymphocyte_Count'])
        D_Dimer=float(request.form['D_Dimer'])
        CRP=float(request.form['CRP'])
        Creatinine=float(request.form['Creatinine'])
        if Age>=5 and Age<=34:
            A=1
        elif Age>=35 and Age<=49:
            A=2
        elif Age>=50 and Age<=64:
            A=3
        elif Age>=65 and Age<=79:
            A=4
        else:
            A=5
          #Lymphocyte  
        if Lymphocyte_Count>=0 and Lymphocyte_Count<=0.49:
            L=1
        elif Lymphocyte_Count>=0.5 and Lymphocyte_Count<=0.99:
            L=2
        elif Lymphocyte_Count>=1 and Lymphocyte_Count<=1.49:
            L=3
        elif Lymphocyte_Count>=1.5 and Lymphocyte_Count<=1.99:
            L=4
        else:
            L=5
        
         #D_Dimer  
        if D_Dimer>=0 and D_Dimer<=499:
            D=1
        elif D_Dimer>=500 and D_Dimer<=999:
            D=2
        elif D_Dimer>=1000 and D_Dimer<=1999:
            D=3
        elif D_Dimer>=2000 and D_Dimer<=3999:
            D=4
        else:
            D=5
            
        #CRP  
        if CRP>=0 and CRP<=19.9:
            CR=1
        elif CRP>=20 and CRP<=59:
            CR=2
        elif CRP>=60 and CRP<=99.9:
            CR=3
        elif CRP>=100 and CRP<=179:
            CR=4
        else:
            CR=5 
            
        #Creatinine  
        if Creatinine>=0 and Creatinine<=0.79:
            C=1
        elif Creatinine>=0.8 and Creatinine<=1.19:
            C=2
        elif Creatinine>=1.2 and Creatinine<=1.79:
            C=3
        elif Creatinine>=1.8 and Creatinine<=2.99:
            C=4 
        else:
            C=5 
            
        output= -0.7606855+1.904726*A-1.964625*L-1.508334*D+0.709297*CR-2.467726*C
        dp=1/(1+math.exp(-output))
        dp=round(dp,4)
        return render_template('result.html', prediction=dp)

if __name__ == '__main__':
	app.run(debug=True)