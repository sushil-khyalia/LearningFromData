from __future__ import division
import math
iterationnumber = 0
u = 1
v = 1
E = (u*math.exp(v)-2*v*math.exp(-u))**2
while E > 10**(-14):
    delu = 2*(u*math.exp(v)-2*v*math.exp(-u))*(math.exp(v)+2*v*math.exp(-u))
    delv = 2*(u*math.exp(v)-2*v*math.exp(-u))*(u*math.exp(v)-2*math.exp(-u))
    u = u - 0.1*delu
    v = v - 0.1*delv
    E = (u*math.exp(v)-2*v*math.exp(-u))**2
    iterationnumber = iterationnumber+1

print("Number of iteration required : " + str(iterationnumber))
print("Final u : " + str(u))
print("Final v : " + str(v))

u = 1
v = 1
E = (u*math.exp(v)-2*v*math.exp(-u))**2
while iterationnumber < 15:
    delu = 2*(u*math.exp(v)-2*v*math.exp(-u))*(math.exp(v)+2*v*math.exp(-u))
    u = u - 0.1*delu
    delv = 2*(u*math.exp(v)-2*v*math.exp(-u))*(u*math.exp(v)-2*math.exp(-u))
    v = v - 0.1*delv
    E = (u*math.exp(v)-2*v*math.exp(-u))**2
    iterationnumber = iterationnumber+1

print("Errors after 15 iterations : "+str(E))
