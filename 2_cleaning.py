import pandas as pd

file_path = "datasets/1_mental-heath-in-tech-2016_20161114.csv"
df = pd.read_csv(file_path)

# Removing self-employed
df = df[df["Are you self-employed?"] != 1]  # Removing self-employed rows
df = df.drop(columns=["Are you self-employed?"])  # Removing a column

# Removing company size column
df = df.drop(columns=["How many employees does your company or organization have?"])

# Focusing on technology-oriented company
df = df[df["Is your employer primarily a tech company/organization?"] != 0]
df = df.drop(columns=["Is your employer primarily a tech company/organization?"])

# Dropping the related empty column "Is your primary role within your company related to tech/IT?"
df = df.drop(columns=df.columns[0])

# Dropping the irrelevant geographic data
df = df.drop(columns=df.columns[56])
df = df.drop(columns=df.columns[55])
df = df.drop(columns=df.columns[54])
df = df.drop(columns=df.columns[53])

# Dropping the sparse data
df = df.drop(columns=df.columns[45])
df = df.drop(columns=df.columns[44])
df = df.drop(columns=df.columns[40])

# Dropping vague previous experiences
df = df.drop(columns=df.columns[39])

# Dropping open-ended answers
df = df.drop(columns=df.columns[35])

# Dropping previous experiences
df = df.drop(columns=df.columns[34])

# Dropping open-ended answers
df = df.drop(columns=df.columns[33])

# Dropping previous experiences
df = df.drop(columns=df.columns[32])

# Dropping the previous experience irrelevant columns
df = df.drop(columns=df.columns[31])
df = df.drop(columns=df.columns[30])
df = df.drop(columns=df.columns[29])
df = df.drop(columns=df.columns[28])
df = df.drop(columns=df.columns[27])
df = df.drop(columns=df.columns[26])
df = df.drop(columns=df.columns[25])
df = df.drop(columns=df.columns[24])
df = df.drop(columns=df.columns[23])
df = df.drop(columns=df.columns[22])
df = df.drop(columns=df.columns[21])
df = df.drop(columns=df.columns[20])

# Dropping the related self-employed empty columns
df = df.drop(columns=df.columns[19])
df = df.drop(columns=df.columns[18])
df = df.drop(columns=df.columns[17])
df = df.drop(columns=df.columns[16])
df = df.drop(columns=df.columns[15])
df = df.drop(columns=df.columns[14])
df = df.drop(columns=df.columns[13])
df = df.drop(columns=df.columns[12])

print(df.info())  # Column details

df.to_csv("datasets/2_cleaned_dataset.csv", index=False)
