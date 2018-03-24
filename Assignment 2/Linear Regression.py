from __future__ import division
import random
import numpy as np

N=100
inSampleErrors = 0
outSampleErrors = 0
for j in range(1000):
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

    w = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(x),x)),np.transpose(x)),y)
    for i in range(N):
        if np.sign(np.dot(x[i],w)) != y[i]:
            inSampleErrors = inSampleErrors+1

    for i in range(1000):
        test_x = random.uniform(-1,1)
        test_y = random.uniform(-1,1)
        if np.sign((test_y-p1_y) - ((p2_y-p1_y)/(p2_x-p1_x))*(test_x-p1_x)) != np.sign(w[0]+test_x*w[1]+test_y*w[2]):
            outSampleErrors = outSampleErrors + 1

N=10
iternationNumber = 0
for j in range(1000):
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

    w = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(x),x)),np.transpose(x)),y)
    for i in range(N):
        if np.sign(np.dot(x[i],w)) != y[i]:
            inSampleErrors = inSampleErrors+1

    while True:
        allClassified = True
        for i in range(N):
            if np.sign(np.dot(x[i],w)) != y[i]:
                allClassified = False
                w = w + y[i]*x[i]
                iternationNumber = iternationNumber + 1
                break
        if allClassified:
            break

print("E_in : "+str(inSampleErrors/100000))
print("E_out : "+str(outSampleErrors/1000000))
print("Average number of iterations : "+str(iternationNumber/1000))
