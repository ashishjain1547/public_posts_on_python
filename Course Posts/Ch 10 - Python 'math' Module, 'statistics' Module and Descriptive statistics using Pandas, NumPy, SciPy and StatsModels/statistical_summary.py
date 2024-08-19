l = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 36, 40, 45, 46, 52, 70]

# Sum of all elements

print(sum(l))

# Count of each items.

from collections import Counter 
print(Counter(l))

# Mean

import statistics as st

print(st.mean(l))

print("Median:", st.median(l))

# Mode

print(st.mode(l))

# Mid-range 

print(st.mean([max(l), min(l)]))

# Other statistical measures

print(st.quantiles(data = l, n = 4)) # [20.0, 25.0, 35.25]
print(st.stdev(l))
print(st.variance(l))

import pandas
l = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 36, 40, 45, 46, 52, 70]
df = pandas.DataFrame(l, columns=['Numbers'])
sum = df['Numbers'].sum()
count_val = df['Numbers'].value_counts()
mode = df['Numbers'].mode().values.tolist()
midrange = (df['Numbers'].max() + df['Numbers'].min()) / 2

print("The sum of the given data using pandas ", sum)
print("\nThe count of values \n", count_val)
print("\nMean of the given data using pandas ", df['Numbers'].mean())
print("\nMedian of the given data using pandas ", df['Numbers'].median())
print("\nMode of the given data using pandas ", mode[0])
print("\nMidrange of the given data using pandas:", midrange)
print("\nStandard deviation for given data using pandas:", df['Numbers'].std())
print("\nVariance for given data using pandas:", df['Numbers'].var())
print("\nQuantiles\n", df['Numbers'].quantile([0.25,0.50,0.75]))
print("\n\n")

import numpy as np

data=np.array(l)
print("Using NumPy\n")
unique_values, counts = np.unique(data, return_counts=True)
quantiles=np.percentile(data,[25,50,75])
print("Sum ",np.sum(data))
print("\nCount of values \n")
for value, count in zip(unique_values, counts):
    print( value, count)   
print("Mean :",np.mean(data))
print("\nMedian:",np.median(data))
print("\nMode:",np.argmax(np.bincount(data)))    
print("\nStandard deviation",np.std(data))
print("\nVariance :",np.var(data))
print("\nQuantiles \n")
print(quantiles[0],quantiles[1],quantiles[2])
print("\n\n")


from scipy import stats 

print("Using SciPy\n")
mode=stats.mode(data)
print("Mode: ", mode.mode[0])

# For count--> scipy.stats.itemfreq()
# Other statistical measures similar to numpy