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