# -*- coding: utf-8 -*-
from math import sinh
def mans_sinuss(x):
 k = 0
 a = x/2
 S = a
 print(" ")
 print("a0 = %6.2f S0 = %6.2f"%(a,S))
 while k<499:
  k = k +1
  R = (x**2)/(2*k*(2*k+1)*2**2)
  a = a * R
  S = S + a
 print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
 k = k + 1
 R = (x**2)/(2*k*(2*k+1)*2**2)
 a = a * R
 S = S + a
 print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
 return S
print("Sinh aprekinasana")
x = float(input("ievadi argumentu (x): "))
y = sinh(x)
print("sin(%.2f) = %6.2f"%(x,y))
yy = mans_sinuss(x)
print("mans sinh(%.2f) = %6.2f"%(x,yy))
print(" ")

print("           500")
print("          _____")
print("          \           2*k+1")
print("           \         x")
print("sinh(x/2) = >   _______________")
print("           /              2*k+1")
print("          /____ (2*k+1)!*2")
print("           k=0")

print("                               2")
print("                              x ")
print("rekurences reizinatajs: ______________")
print("                                     2")
print("                        2*k*(2*k+1)*2")
