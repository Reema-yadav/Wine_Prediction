import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression


model = joblib.load('Wine_Prediction_Model.pkl')

Scaler = joblib.load('standard_scaler.pkl')



def input(a,b,c,d,e,f,g,h,i,j,k,l):
    inputs = [{'fixed_acidity':float(a), 'volatile_acidity':float(b), 'citric_acid':float(c), 'residual_sugar':float(d), 'chlorides':float(e), 'free_sulfur_dioxide':float(f), 'total_sulfur _ioxide':float(g), 'density':float(h), 'pH':float(i), 'sulphates':float(j), 'alcohol':float(k), 'type':l}]
    
          
    df = pd.DataFrame(inputs) 
    

    
    if not set(df['type']).issubset ({'red', 'white'}):
        print("Entered type is wromg")
    else:
        df['type'] = df['type'].replace({'red':0, 'white':1})     
        
    df_2d = df.values.reshape(1,-1)   
        
    scaled_df = Scaler.transform(df_2d)
    
    return scaled_df

  

    

def prediction(input):
    
    PREDICTION = model.predict(input)
    
    
    return PREDICTION[0]
    
    

def answer(result):
    if result == 0:
        return 'Legit'
    else:
        return 'Fraud'


          
        
    
    
    
    
   
    
    
    
    
    
    
   