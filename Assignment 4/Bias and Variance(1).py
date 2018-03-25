from __future__ import division
import numpy as np
import math
import random

abar = 0
for i in range(1000000):
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    abar = abar + ((math.sin(math.pi*x1)*x1+math.sin(math.pi*x2)*x2)/(x1*x1 + x2*x2))/1000000
variance = 0
for i in range(1000000):
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    variance = variance + (1/1000000)*(1/2)*(2/3)*(((math.sin(math.pi*x1)*x1+math.sin(math.pi*x2)*x2)/(x1*x1 + x2*x2))-abar)*(((math.sin(math.pi*x1)*x1+math.sin(math.pi*x2)*x2)/(x1*x1 + x2*x2))-abar)

bias = (abar*abar)/3 + 1/2 - (2*abar)/math.pi
print("ghat(x) : " + str(abar) + "x")
print("Bias : " + str(bias))
print("Variance : " + str(variance))
