import pandas as pd

df = pd.DataFrame(
    {
        "Customerkeycode": [
            "B01:B14:110083",
            "B02:B15:110084"
        ]
    }
)

df['PlanningCustomerSuperGroupCode'] = df['Customerkeycode'].apply(lambda x: x.split(":")[0])
df['DPGCode'] = df['Customerkeycode'].apply(lambda x: x.split(":")[1])
df['APGCode'] = df['Customerkeycode'].apply(lambda x: x.split(":")[2])

df_rep = df.drop("Customerkeycode", axis = 1)

print(df_rep)
