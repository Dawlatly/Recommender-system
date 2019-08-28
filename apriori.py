# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 22:09:39 2017

@author: Mahmoud Dawlatly
"""

import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('FYP.csv')

# Association Rule Learning Using Apriori
from apyori import apriori
customer_ID=dataset.iloc[:, [5,10]].values

customer_ID = customer_ID[customer_ID[:,0].argsort()]
anlist=[]
anlist.append([str('Labels')])
for i in range(0,9426):
    if(i==0):
        continue
    if(customer_ID[i][0]==customer_ID[i-1][0]):
        anlist[-1].append(str(customer_ID[i][1]))
    else:
        anlist[-1]=list(set(anlist[-1]))
        anlist.append([str(customer_ID[i][1])])

rules = apriori(anlist, min_support=0.02,min_confidence=0.2,min_lift=1.4,min_length=2)
results = list(rules)
# This function takes as argument your results list and return a tuple list with the format:
# [(rh, lh, support, confidence, lift)] 
def inspect(results):
    rh          = [tuple(result[2][0][0]) for result in results]
    lh          = [tuple(result[2][0][1]) for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(rh, lh, supports, confidences, lifts))
 
# this command creates a data frame to view
resultDataFrame=pd.DataFrame(inspect(results))
lhs = []
rhs = []
finalLhs = []
finalRhs = []
for i in range(0,resultDataFrame.__len__()):
    lhs.append(resultDataFrame[1][i][0])
    
for j in range(0,resultDataFrame.__len__()):
    rhs.append(resultDataFrame[0][j])
    
finalLhs.append(lhs[0])
finalLhs.append(lhs[1])
finalLhs.append(lhs[2])
finalLhs.append(lhs[4])
finalLhs.append(lhs[5])
finalLhs.append(lhs[9])
finalLhs.append(lhs[10])
finalLhs.append(lhs[16])
finalLhs.append(lhs[17])
finalLhs.append(lhs[21])
finalLhs.append(lhs[24])
finalLhs.append(lhs[32])
finalLhs.append(lhs[33])
finalLhs.append(lhs[35])
finalLhs.append(lhs[42])
finalLhs.append(lhs[47])
finalLhs.append(lhs[50])
finalLhs.append(lhs[51])
finalLhs.append(lhs[55])

finalRhs.append(rhs[0])
finalRhs.append(rhs[1])
finalRhs.append(rhs[2])
finalRhs.append(rhs[4])
finalRhs.append(rhs[5])
finalRhs.append(rhs[9])
finalRhs.append(rhs[10])
finalRhs.append(rhs[16])
finalRhs.append(rhs[17])
finalRhs.append(rhs[21])
finalRhs.append(rhs[24])
finalRhs.append(rhs[32])
finalRhs.append(rhs[33])
finalRhs.append(rhs[35])
finalRhs.append(rhs[42])
finalRhs.append(rhs[47])
finalRhs.append(rhs[50])
finalRhs.append(rhs[51])
finalRhs.append(rhs[55])