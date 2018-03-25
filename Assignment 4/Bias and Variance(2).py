from __future__ import division
import random
import math

# Option A

bhat = 0
for i in range(1000000):
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    bhat = bhat + (math.sin(math.pi*x1)+math.sin(math.pi*x2))/2000000

variance = 0
for i in range(1000000):
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    bhattest = (math.sin(math.pi*x1)+math.sin(math.pi*x2))/2
    variance = variance+((bhat-bhattest)**2)/1000000

bias = bhat**2 + 0.5
print("====================================")
print("Option A")
print("Bias : "+str(bias))
print("Variance : "+str(variance))
print("Eout : "+str(bias+variance))
print("====================================")

# Option B

abar = 0
for i in range(1000000):
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    abar = abar + ((math.sin(math.pi*x1)*x1+math.sin(math.pi*x2)*x2)/(x1*x1 + x2*x2))/1000000
variance = 0
for i in range(1000000):
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    abartest = ((math.sin(math.pi*x1)*x1+math.sin(math.pi*x2)*x2)/(x1*x1 + x2*x2))
    variance = variance + (1/1000000)*(1/3)*(abartest-abar)**2
bias = (abar*abar)/3 + 1/2 - (2*abar)/math.pi

print("====================================")
print("Option B")
print("Bias : "+str(bias))
print("Variance : "+str(variance))
print("Eout : "+str(bias+variance))
print("====================================")

# Option C

abar = 0
bhat = 0
for i in range(1000000):
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    abar = abar + ((math.sin(math.pi*x1)-math.sin(math.pi*x2))/(x1-x2))/1000000
    bhat = bhat + ((math.sin(math.pi*x2)*x1-math.sin(math.pi*x1)*x2)/(x1-x2))/1000000

variance = 0
for i in range(1000000):
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    abartest = ((math.sin(math.pi*x1)-math.sin(math.pi*x2))/(x1-x2))
    bhattest = ((math.sin(math.pi*x2)*x1-math.sin(math.pi*x1)*x2)/(x1-x2))
    variance = variance + (1/1000000)*((1/3)*((abartest-abar)**2) + (bhattest-bhat)**2)

bias = (abar*abar)/3 + 1/2 - (2*abar)/math.pi + bhat**2
print("====================================")
print("Option C")
print("Bias : "+str(bias))
print("Variance : "+str(variance))
print("Eout : "+str(bias+variance))
print("====================================")

#Option D

abar = 0
for i in range(1000000):
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    abar = abar + ((math.sin(math.pi*x1)*x1**2+math.sin(math.pi*x2)*x2**2)/(x1**4 + x2**4))/1000000
variance = 0
for i in range(1000000):
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    abartest = ((math.sin(math.pi*x1)*x1**2+math.sin(math.pi*x2)*x2**2)/(x1**4 + x2**4))
    variance = variance + (1/1000000)*(1/5)*(abartest-abar)**2

bias = 0.5 + abar**2/5
print("====================================")
print("Option D")
print("Bias : "+str(bias))
print("Variance : "+str(variance))
print("Eout : "+str(bias+variance))
print("====================================")

# Option E

abar = 0
bhat = 0
for i in range(1000000):
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    abar = abar + ((math.sin(math.pi*x1)-math.sin(math.pi*x2))/(x1**2-x2**2))/1000000
    bhat = bhat + ((math.sin(math.pi*x2)*x1**2-math.sin(math.pi*x1)*x2**2)/(x1-x2))/1000000

variance = 0
for i in range(1000000):
    x1 = random.uniform(-1,1)
    x2 = random.uniform(-1,1)
    abartest = ((math.sin(math.pi*x1)-math.sin(math.pi*x2))/(x1**2-x2**2))
    bhattest = ((math.sin(math.pi*x2)*x1**2-math.sin(math.pi*x1)*x2**2)/(x1-x2))
    variance = variance + (1/1000000)*(0.2*(abar-abartest)**2 + 2*(abar-abartest)*(bhat-bhattest)/3 + (bhat-bhattest)**2)

bias = 0.5 + 0.2*abar**2 + 2*abar*bhat/3 + bhat**2 + 0.5

print("====================================")
print("Option E")
print("Bias : "+str(bias))
print("Variance : "+str(variance))
print("Eout : "+str(bias+variance))
print("====================================")
