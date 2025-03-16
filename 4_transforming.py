import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

file_path = "datasets/3_imputed_dataset.csv"
df = pd.read_csv(file_path)

# Convert the entire DataFrame to lowercase -> UPPERCASE should equal lowercase values
df = df.map(lambda x: x.lower() if not isinstance(x, int) else x)

"""gender"""
# Cleaning a gender column -> "male" and "male." should equal.
df[df.columns[24]] = df[df.columns[24]].str.replace(r'[ .()-;]', '', regex=True)


def sort_string(string):
    return ''.join(sorted(string))


# Sorting the gender column - avoiding duplicates cismale should equal malecis
df[df.columns[24]] = df[df.columns[24]].apply(sort_string)

"""positions and diagnosis"""
# Split the diagnosis and positions column by "|"
positions_split = df[df.columns[25]].str.split('|')
diagnosis_split = df[df.columns[19]].str.split('|')

# Create a set of all unique diagnosis / positions
all_positions = set([item for sublist in positions_split for item in sublist])
all_diagnosis = set([item for sublist in diagnosis_split for item in sublist])

# Add one-hot encoded columns for each diagnosis / position
for position in all_positions:
    df[position] = positions_split.apply(lambda x: 1 if position in x else 0)

for diagnosis in all_diagnosis:
    df[diagnosis] = diagnosis_split.apply(lambda x: 1 if diagnosis in x else 0)

# Drop the original 'diagnosis' / 'position' column
df = df.drop(columns=[df.columns[25]])
df = df.drop(columns=[df.columns[19]])

"""age"""
# eyeballing the Quartiles
# print(df[df.columns[22]].describe())
bins = [0, 28, 32, 37, 99]
labels = [0, 1, 2, 3]

df['age_group'] = pd.cut(df[df.columns[22]], bins=bins, labels=labels)
encoder = OrdinalEncoder(categories=[labels])
df["age_group"] = encoder.fit_transform(df[["age_group"]])

df = df.drop(columns=[df.columns[22]])

"""final one-hot encoding"""
df = pd.get_dummies(df, dtype=int)

df.to_csv("datasets/4_transformed_dataset.csv", index=False)
