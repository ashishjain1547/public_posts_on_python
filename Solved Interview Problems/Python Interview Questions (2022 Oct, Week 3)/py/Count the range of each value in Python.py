"""
I have dataset of student's scores for each subject.

StuID  Subject Scores                
1      Math    90
1      Geo     80
2      Math    70
2      Geo     60
3      Math    50
3      Geo     90
Now I want to count the range of scores for each subject like 0 < x <=20, 20 < x <=30 and get a dataframe like this:

Subject  0-20  20-40 40-60 60-80 80-100                 
Math       0     0     1     1     1
Geo        0     0     0     1     2    
The given dataset is just a sample of the data I am working on. My dataset has more than 1000 line. How can I do it? Thank you!
"""

import pandas as pd

df = pd.DataFrame({
    "StuID": [1,1,2,2,3,3],
    "Subject": ['Math', 'Geo', 'Math', 'Geo', 'Math', 'Geo'],
    "Scores": [90, 80, 70, 60, 50, 90]
})

bins = list(range(0, 100+1, 20))
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
labels = [f'{a}-{b}' for a,b in zip(bins, bins[1:])]
# ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']

out = (pd.crosstab(df['Subject'], pd.cut(df['Scores'], bins=bins,
                                         labels=labels, ordered=True, right=False))
          .reindex(labels, axis=1, fill_value=0)
      )

print(out)