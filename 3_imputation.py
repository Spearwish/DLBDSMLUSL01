import pandas as pd
import numpy as np

file_path = "datasets/2_cleaned_dataset.csv"
df = pd.read_csv(file_path)

"""gender"""
# Setting 1 NaN gender to "unknown"
gender_column_name = df.columns[24]
df[gender_column_name] = df[gender_column_name].fillna("unknown")

"""diagnosis"""
# Filling gaps for those who were not diagnosed
diagnosis_column_name = df.columns[18]
condition_column_name = df.columns[19]
df.loc[(df[diagnosis_column_name] == "No") & (df[condition_column_name].isna()), condition_column_name] = "no diagnosis"

# Setting 2 NaN diagnosis to unknown
df[condition_column_name] = df[condition_column_name].fillna("unknown")

"""
There seems to be some correlation between mental healthcare coverage and  "Do you know the options for mental health care ..." columns.
Lets fill the missing values in the second (index 1) column based on probability appearance.
"""
m_h_c_coverage = df.columns[0]
m_h_c_options = df.columns[1]
# Combinations counts
combinations = df.groupby([m_h_c_coverage, m_h_c_options]).size().reset_index(name='count')

# Standardized probability for each mental healthcare coverage response type
combinations['probability'] = combinations.groupby(m_h_c_coverage)['count'].transform(lambda x: x / x.sum())

print("Counts and normalized occurrences:\n", combinations.to_string())


def impute_probabilistically(row, combinations):
    if pd.isna(row[m_h_c_options]):
        # Boolean mask for retrieving the correct probabilities for missing m_h_c_options value
        prob_df = combinations[combinations[m_h_c_coverage] == row[m_h_c_coverage]]
        # Randomly choose a value for m_h_c_options column based on the probabilities
        imputed_value = np.random.choice(prob_df[m_h_c_options], p=prob_df['probability'])
        return imputed_value
    else:
        return row[m_h_c_options]


df[m_h_c_options] = df.apply(impute_probabilistically, combinations=combinations, axis=1)

"""age"""
# Everything that exceeds age value 99 or fall below 18 is changed to column mean
age_column_name = df.columns[23]
print("Age column basic stats:\n",df[age_column_name].describe())
df.loc[(df[age_column_name] > 99) | (df[age_column_name] < 18), age_column_name] = round(df[age_column_name].mean())

# Use for DataFrame column overview
print(df.info())
print("Age column basic stats:\n",df[age_column_name].describe())

df.to_csv("datasets/3_imputed_dataset.csv", index=False)
