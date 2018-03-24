from __future__ import division
import random

count_c1 = 0
count_crand = 0
count_cmin = 0
for i in range(100000):
    crand = random.randint(0,999)
    cmin = 11
    for j in range(1000):
        heads = 0
        for k in range(10):
            heads = heads + random.randint(0,1)
        if j==0:
            count_c1 = count_c1+heads
        if j==crand:
            count_crand = count_crand+heads
        if heads < cmin:
            cmin = heads
    count_cmin = count_cmin + cmin

print("Average value for first coin : " + str(count_c1/1000000))
print("Average value for random coin : " + str(count_crand/1000000))
print("Average value for least occuring coin : " + str(count_cmin/1000000))
