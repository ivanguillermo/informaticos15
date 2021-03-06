#! /usr/bin/python

#Aproxime el valor de ln(1,3) usando un Polinomio de interpolacion de Lagrange de grado 2
#que pase por los puntos x0=1, x1=1.5 y x2=2. Determine cuan buena es su aproximacion

#Definimos la f(x) que queremos aproximar

import math
def f(x):
	r= math.log(x);
	return r 

#Los puntos por los que debe pasar el polinomio
x0= 1
x1= 1.5
x2= 2 

def L(x,a,b,c):
	r= ((x - c)*(x - b))/((a - c)*(a - b))
	return r

def P2(x):
	L02= L(x,x0,x2,x1)
	L12= L(x,x1,x2,x0)
	L22= L(x,x2,x1,x0)
	r = f(x0)*L02 + f(x1)*L12 + f(x2)*L22
	return r

print "El Polinomio de Lagrange de grado 2 tiene valor " + str(P2(1.3))

#Calcular error
def Error(x):
	e= math.fabs(f(x)-P2(x))
	return e

print "El Error es " + str(Error(1.3))
