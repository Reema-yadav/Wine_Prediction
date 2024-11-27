import pandas as pd
import module
import warnings
warnings.filterwarnings("ignore")

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/Wine_Prediction', methods = ['POST'])
def input():
    data = request.form
    
    if request.method  == 'POST':
        a = data['a']
        b = data['b']
        c = data['c']
        d = data['d']
        e = data['e']
        f = data['f']
        g = data['g']
        h = data['h']
        i = data['i']
        j = data['j']
        k = data['k']
        l = data['l']
        
        
    input_for_prediction = module.input(a,b,c,d,e,f,g,h,i,j,k,l)
    
    
    input_prediction = module.prediction(input_for_prediction)
    
    
    final_result = module.answer(input_prediction)
    
    
    return jsonify(f'The Given Wine is : {final_result}')



if __name__ =="__main__":
    app.run()

        
        
        
        





      
