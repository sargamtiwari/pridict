# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:05:12 2019

@author: TWS1KOR
"""

import pandas as pd
df=pd.read_csv('emp_data.csv',sep=',', parse_dates=['Emp ID'],index_col='Emp ID')
df=df.dropna()
train=df[:17]
test=df[17:]

colgp=df.columns
print(len(colgp))
from statsmodels.tsa.vector_ar.var_model import VAR

model = VAR(endog=train)
model_fit = model.fit()
prediction = model_fit.forecast(model_fit.y, steps=4)
result= pd.DataFrame(index=range(0,len(prediction)),columns=[colgp]) 

for j in range(0,119):
    for i in range(0, len(prediction)):
     if prediction[i][j]<2:
           prediction[i][j]=0; 
     result.iloc[i][j] =round( prediction[i][j]) 
     
result.columns = colgp
result.index=['Week 18','Week 19','Week 20','Week 21']
print(result.to_json())