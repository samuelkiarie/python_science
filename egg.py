# how to cook a perfect egg
from math import *
from numpy import *
M = 47 #grams
m = 67 #grams
d = 1.038 #g/cm**-3
c = 3.7 # Jg**-1K**-1
k = 5.4*10**-3 #Wcm**-1K**-1
# to original temp
#tw temp water boiling
to = 4
tw = 100
ty = 70
to2 = 20
A =float(M**(2/3)*c*d**(1/3))
B =float(k*pi**2*((4*pi)/3)**(2/3))
C =float(0.76*((to - tw)/(ty - tw)))
D =log(C)
T =float((A/B)*D)
print T
