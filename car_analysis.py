import pandas as pd

df= pd.read_csv ("C:/Users/Adnan/Python/car_details.csv")

# print(df.info())
# print(df.shape)

# Find the no. of null values and the column
# print(df.isnull().sum())


# print(df.loc[df['Make'].isnull()])

# Remove null rows
df.dropna(axis=0, how='all', inplace=True, ignore_index=True)

