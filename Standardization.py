
import pandas as pd

#loading data set
seed = pd.read_csv("C:/Users/hp/Desktop/DataSets/Seeds_data.csv")

seed.info()   #For data types and non or null values
# data has no na or nall values 

seed.describe() # for mean ,min, max, IQR 


EDA=pd.DataFrame({"columns_name ":seed.columns,
                  "mean":seed.mean(),
                  "median":seed.median(),
                  "mode":seed.mode(),
                  "standard_deviation":seed.std(),
                  "variance":seed.var(),
                  "skewness":seed.skew(),
                  "kurtosis":seed.kurt()})
EDA            

import matplotlib.pyplot as plt # for data visualization 
# let's find outliers in seed
#boxplot for every column
for column in seed:
    plt.figure()
    seed.boxplot([column])

seed.columns
boxplot = seed.boxplot(column= ['Area', 'Perimeter ', 'Compactness', 'length', 'Width',
       'Assymetry_coeff', 'len_ker_grove', 'Type'])

# Standardization function using z std. all are continuous data.
def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)

# Standardization data frame (considering the numerical part of data)
seed_norm = norm_func(seed.iloc[:,0:7])
seed_norm.describe()
