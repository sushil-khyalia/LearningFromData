from __future__ import division
import random
import numpy as np

N=1000
inSampleErrors = 0
ga = np.array([-1,-0.05,0.08,0.13,1.5,1.5])
gb = np.array([-1,-0.05,0.08,0.13,1.5,15])
gc = np.array([-1,-0.05,0.08,0.13,15,1.5])
gd = np.array([-1,-1.5,0.08,0.13,0.05,0.05])
ge = np.array([-1,-0.05,0.08,1.5,0.15,0.15])
inSampleErrorsa = 0
inSampleErrorsb = 0
inSampleErrorsc = 0
inSampleErrorsd = 0
inSampleErrorse = 0
outSampleErrors = 0
for j in range(1000):
    x = np.zeros((N,3))
    z = np.zeros((N,6))
    y = np.zeros(N)
    for i in range(N):
        x[i][0] = 1
        x[i][1] = random.uniform(-1,1)
        x[i][2] = random.uniform(-1,1)
        z[i][0] = 1
        z[i][1] = x[i][1]
        z[i][2] = x[i][2]
        z[i][3] = x[i][1]*x[i][2]
        z[i][4] = x[i][1]**2
        z[i][5] = x[i][2]**2
        y[i] = np.sign(x[i][1]**2 + x[i][2]**2 -0.6)

    for i in np.random.choice(1000, 100, replace=False):
        y[i] = -1*y[i]

    w = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(x),x)),np.transpose(x)),y)
    for i in range(N):
        if np.sign(np.dot(x[i],w)) != np.sign(x[i][1]**2 + x[i][2]**2 -0.6):
            inSampleErrors = inSampleErrors+1

    for i in range(N):
        if np.sign(np.dot(z[i],ga)) != np.sign(x[i][1]**2 + x[i][2]**2 -0.6):
            inSampleErrorsa = inSampleErrorsa+1

    for i in range(N):
        if np.sign(np.dot(z[i],gb)) != np.sign(x[i][1]**2 + x[i][2]**2 -0.6):
            inSampleErrorsb = inSampleErrorsb+1

    for i in range(N):
        if np.sign(np.dot(z[i],gc)) != np.sign(x[i][1]**2 + x[i][2]**2 -0.6):
            inSampleErrorsc = inSampleErrorsc+1

    for i in range(N):
        if np.sign(np.dot(z[i],gd)) != np.sign(x[i][1]**2 + x[i][2]**2 -0.6):
            inSampleErrorsd = inSampleErrorsd+1

    for i in range(N):
        if np.sign(np.dot(z[i],ge)) != np.sign(x[i][1]**2 + x[i][2]**2 -0.6):
            inSampleErrorse = inSampleErrorse+1

    for i in range(1000):
        test_x = random.uniform(-1,1)
        test_y = random.uniform(-1,1)
        z_test = np.array([1,test_x,test_y,test_x*test_y,test_x**2,test_y**2])
        if np.sign(np.dot(z_test,ga)) != np.sign(test_x**2 + test_y**2 -0.6):
            outSampleErrors = outSampleErrors + 1

print("E_in : "+str(inSampleErrors/1000000))
print("Error in a : "+str(inSampleErrorsa/1000000))
print("Error in b : "+str(inSampleErrorsb/1000000))
print("Error in c : "+str(inSampleErrorsc/1000000))
print("Error in d : "+str(inSampleErrorsd/1000000))
print("Error in e : "+str(inSampleErrorse/1000000))
print("Expected Out Sample Error : "+str(outSampleErrors/1000000))
