import pandas as pd
import sys

data = sys.argv[1]

# Basic CSV import
df = pd.read_csv(data)

# To count rows in a dataframe
df.count()

# To remove any columns that are blank or missing:
df.dropna(inplace = True)

# To remove any duplicate rows
df.drop_duplicates(inplace = True)

# To write the dataframe out to a new CSV
df.to_csv('cleaned.csv')
