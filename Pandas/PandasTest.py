from operator import index

import pandas as pd

mydataset = {
    'cars':["volvo","BMW","Audi"],
    'passings':[3,7,2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
print(pd.__version__)
a = [1,7,3]
myvar = pd.Series(a)
print(myvar)
myvar = pd.Series(a,index=["x","y","z"])
print("labels \n",myvar)
print(myvar["x"])
calories = {"day1":420,"day2":340,"day3":780}
myvar = pd.Series(calories,index=["day1","day2"])
print(myvar)