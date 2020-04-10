# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
def correlationCoefficient(n,xSum,ySum,xySum,x2Sum,y2Sum):
    r = (n*xySum-xSum*ySum)/(math.sqrt(n*x2Sum-xSum**2)*math.sqrt(n*y2Sum-ySum**2))
    print(r)

def leastSquaresLine(n,xSum,ySum,xySum,x2Sum):
    m = (n*xySum-xSum*ySum)/(n*x2Sum-xSum**2)
    b = (ySum - m*xSum)/n
    print(m,b)


xVals = [5,15,25,35,45,55,65,75,85,95]
yVals = [6.041,4.982,3.681,3.167,2.392,1.538,0.923,0.236,-0.637,-1.245]

xyVals = [0,0,0,0,0,0,0,0,0,0]
x2Vals = [0,0,0,0,0,0,0,0,0,0]
y2Vals = [0,0,0,0,0,0,0,0,0,0]

for n in range(0,len(xVals)):
    xyVals[n] = xVals[n]*yVals[n]
    x2Vals[n] = xVals[n]**2
    y2Vals[n] = yVals[n]**2
    
xSum = sum(xVals)
ySum = sum(yVals)
xySum = sum(xyVals)
x2Sum = sum(x2Vals)
y2Sum = sum(y2Vals)

correlationCoefficient(len(xVals),xSum,ySum,xySum,x2Sum,y2Sum)
leastSquaresLine(len(xVals), xSum, ySum, xySum, x2Sum)