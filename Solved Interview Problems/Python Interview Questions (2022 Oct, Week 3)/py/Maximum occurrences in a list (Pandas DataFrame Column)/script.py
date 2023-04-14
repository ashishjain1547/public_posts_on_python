import pandas as pd

data = {'Date': ['2022/09/01', '2022/09/02', '2022/09/03', '2022/09/04', '2022/09/05','2022/09/01', '2022/09/02', '2022/09/03', '2022/09/04', '2022/09/05','2022/09/01', '2022/09/02', '2022/09/03', '2022/09/04', '2022/09/05'],
        'Runner': ['Runner A', 'Runner A', 'Runner A', 'Runner A', 'Runner A','Runner B', 'Runner B', 'Runner B', 'Runner B', 'Runner B','Runner C', 'Runner C', 'Runner C', 'Runner C', 'Runner C'],
        'Training Time': ['less than 1 hour', 'less than 1 hour', 'less than 1 hour', 'less than 1 hour', '1 hour to 2 hour','less than 1 hour', '1 hour to 2 hour', 'less than 1 hour', '1 hour to 2 hour', '2 hour to 3 hour', '1 hour to 2 hour ', '2 hour to 3 hour' ,'1 hour to 2 hour ', '2 hour to 3 hour', '2 hour to 3 hour']
        }

df = pd.DataFrame(data)
s = df.groupby(['Runner', 'Training Time'], as_index=False).size()
s.columns = ['Runner', 'Training Time', 'Size']

print(s)

r = s.groupby(['Runner'], as_index=False)['Size'].max()

print(r)

df_list = []
for index, row in r.iterrows():
    temp_df = s[(s['Runner'] == row['Runner']) & (s['Size'] == row['Size'])]
    df_list.append(temp_df)

df_report = pd.concat(df_list)
print(df_report)
    
df_report.to_csv('report.csv', index = False)
