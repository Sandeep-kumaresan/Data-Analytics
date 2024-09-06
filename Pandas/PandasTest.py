import pandas as pd

mydataset = {
    'cars':["volvo","BMW","Audi"],
    'passings':[3,7,2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)