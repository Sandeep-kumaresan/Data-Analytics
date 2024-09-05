import numpy as np
import pandas as pd
num1=4
num2=6
gcd=np.gcd(num1,num2)
print(gcd)
lcm = np.lcm(num1,num2)
print(lcm)
arr=np.array([3,6,9])
gcdred = np.gcd.reduce(arr)
print(gcdred)
arr2 = np.array([3,6,9])
lcmred = np.lcm.reduce(arr2)
print(lcmred)