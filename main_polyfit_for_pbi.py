# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:26:53 2019

@author: PeerapongE
"""


from sklearn.preprocessing import PolynomialFeatures # ใช้ สร้าง polynomial
from sklearn.linear_model import LinearRegression # Module ที่เอาไว้ใช้ทำ linear regression

import matplotlib.pyplot as plt # เอาไว้ plot

import numpy as np
import pandas as pd


def func_regress_poly(df, x_name, y_name, cat_name, nPoly):
    # return function
    # y = a + b1*x^2 + b2*x^2 + b3*x^3
    
    df.dropna(inplace = True) # drop nan
    
    cat_list = df[cat_name].unique().tolist() # list of unique value of cat_name
    
    
    color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    
    #plt.figure((12,5))
    
    for (category,color_cat) in zip(cat_list, color_list):
        print('Category = %s, color = %s'%(category,color_cat))
        dfCat = df[df[cat_name] == category]
        
        X = dfCat[[x_name]]
        y = dfCat[y_name]
        
        # Fitting Polynomial
        poly = PolynomialFeatures(degree      = nPoly,
                                 include_bias = None)
        
        X_ = poly.fit_transform(X)
        
        lg = LinearRegression()
        lg.fit(X_, y)
        
        # output
        a  = lg.intercept_
        b  = lg.coef_
        #r2 = lg.score(X_, y)
        
        X_plot = np.linspace(X.min(),X.max(),50)
        Y_plot = a + b[0]*X_plot + b[1] * (X_plot ** 2)    
        
        plt.scatter(X, y, color = color_cat, alpha = 0.5, label = category)  # scatter 
        plt.plot(X_plot, Y_plot, color = color_cat) # line
        
    
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title(('Plot between %s and %s categorized by %s')%(x_name, y_name, cat_name))
    #plt.savefig('savefig.jpg')
    plt.legend()
    
    plt.show()
    
#    return(a,b,r2)

# df = pd.read_excel('Raw.xlsx')

# df = pd.read_excel('input_test_data.xlsx')


x_name   = 'MD'
y_name   = 't'
cat_name = 'year'
nPoly  = 2

func_regress_poly(df, x_name, y_name , cat_name, nPoly)



    