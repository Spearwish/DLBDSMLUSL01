import pandas as pd

file_path = "datasets/4_transformed_dataset.csv"
df = pd.read_csv(file_path)

from sklearn.decomposition import PCA

# Applying the PCA
pca = PCA().fit(df)

# Getting the explained variance ratio (percentage of variance explained by each component)
explained_variance = pca.explained_variance_ratio_
print("explained_variance:", explained_variance)  # The first 2 PCs accounts only for 21 % of variance explanation.

# Extracting the eigenvectors
eig_vecs = pca.components_

# Extracting the feature names
feature_names = df.columns

# Transposing eigenvectors in a Data Frame
eig_vecs_df = pd.DataFrame(eig_vecs.T, columns=[f'PC{i + 1}' for i in range(eig_vecs.shape[0])], index=feature_names)

# Features that contribute to most variance across all PCs
ranking = eig_vecs_df.abs().sum(axis=1).sort_values(ascending=False)

# Retrieving the top 20 features
top_features = ranking.head(20)

# Printing the top feature names
result = top_features.index.tolist()
print(f"top {len(result)} features:", result)
