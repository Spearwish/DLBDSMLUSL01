import pandas as pd

file_path = "datasets/4_transformed_dataset.csv"
df = pd.read_csv(file_path)

import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from matplotlib import pyplot as plt
import seaborn as sns

# Thresholding with VarianceThreshold. Using correlation without it gave us results that are sparse in data points.
selector = VarianceThreshold(threshold=0.10)
selector.fit(df)

# Getting the boolean mask of selected features
selected_columns_mask = selector.get_support()

# Getting the names of the selected columns
selected_columns = df.columns[selected_columns_mask]

# Creating a new DataFrame with only the selected columns
df = df[selected_columns]

"""1 st correlation matrix for selection"""
# Both Pearson and Spearman correlations output the same result, I suppose it is due to one-hot encoding nature.
cor_mat = df.corr(method='pearson')  # df.corr(method='spearman')

# In the next step we will be choosing based on absolute range, keeping the matrix intact would result in every column satisfying the condition.
# Setting the perfect self-correlation diagonal to NaN values.
np.fill_diagonal(cor_mat.values, np.nan)

correlated_columns = [col for col in cor_mat.columns if any(abs(cor_mat[col]) > 0.4525)]

df = df.drop(columns=correlated_columns)

"""2 st correlation matrix for visualisation"""
# Printing the top feature names
result = df.columns
print(f"top {len(result)} features:", result)

cor_mat = df.corr(method='pearson')  # df.corr(method='spearman')

np.fill_diagonal(cor_mat.values, np.nan)

plt.figure(figsize=(12, 10))
ax = sns.heatmap(cor_mat, vmin=-1, vmax=1, annot=False, fmt="f")
plt.show()


