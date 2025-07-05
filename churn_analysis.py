import pandas as pd

df = pd.read_csv(r"C:\Users\asus\Downloads\Customer_churn\Customer-Churn_data.csv")
print(df.head())

df.head()           # Shows first 5 rows
df.info()           # Shows data types and nulls
df.describe()       # Shows summary statistics (for numeric columns)
df.isnull().sum()
df=df.dropna()

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
print(df.head())

