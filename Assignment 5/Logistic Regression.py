from __future__ import division
import random
import math
import numpy as np

N = 100
totalepochs=0
outSampleErrors = 0

for j in range(100):
    x = np.zeros((N,3))
    y = np.zeros(N)
    p1_x = random.uniform(-1,1)
    p2_x = random.uniform(-1,1)
    p1_y = random.uniform(-1,1)
    p2_y = random.uniform(-1,1)
    for i in range(N):
        x[i][0] = 1
        x[i][1] = random.uniform(-1,1)
        x[i][2] = random.uniform(-1,1)
        y[i] = np.sign((x[i][2]-p1_y) - ((p2_y-p1_y)/(p2_x-p1_x))*(x[i][1]-p1_x))

    wprev = np.zeros(3)
    w = np.zeros(3)
    for i in np.random.permutation(N):
        w = w + 0.01*(y[i]/(1+math.exp(y[i]*np.dot(x[i],w))))*x[i]
    totalepochs = totalepochs+1
    while np.linalg.norm(w-wprev) > 0.01:
        wprev = w
        for i in np.random.permutation(N):
            w = w + 0.01*(y[i]/(1+math.exp(y[i]*np.dot(x[i],w))))*x[i]
        totalepochs = totalepochs+1

    for i in range(1000):
        test_x = np.zeros(3)
        test_x[0] = 1
        test_x[1] = random.uniform(-1,1)
        test_x[2] = random.uniform(-1,1)
        test_y = np.sign((test_x[2]-p1_y) - ((p2_y-p1_y)/(p2_x-p1_x))*(test_x[1]-p1_x))
        outSampleErrors = outSampleErrors + math.log(1+math.exp(-1*test_y*np.dot(test_x,w)))

print("Average epochs : " + str(totalepochs/100))
print("Eout : " + str(outSampleErrors/100000))
