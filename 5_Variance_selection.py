import pandas as pd

file_path = "datasets/4_transformed_dataset.csv"
df = pd.read_csv(file_path)

from sklearn.feature_selection import VarianceThreshold

selector = VarianceThreshold(threshold=0.2375)
selector.fit(df)

# Getting the boolean mask of selected features
selected_columns_mask = selector.get_support()

# Getting the names of the selected columns
selected_columns = df.columns[selected_columns_mask]

# Printing the top feature names
result = selected_columns
print(f"top {len(result)} features:", result)