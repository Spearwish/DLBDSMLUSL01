final_features = ['back-end developer', 'age_group',
                  'Do you think that discussing a mental health disorder with your employer would have negative consequences?_yes',
                  'How willing would you be to share with friends and family that you have a mental illness?_somewhat open',
                  'How willing would you be to share with friends and family that you have a mental illness?_very open',
                  'Does your employer provide mental health benefits as part of healthcare coverage?_yes',
                  'Do you think that discussing a mental health disorder with your employer would have negative consequences?_no',
                  'Do you feel that being identified as a person with a mental health issue would hurt your career?_maybe',
                  'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?_maybe',
                  'Do you currently have a mental health disorder?_no',
                  'Do you currently have a mental health disorder?_yes']

import pandas as pd
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "datasets/4_transformed_dataset.csv"
df = pd.read_csv(file_path, usecols=final_features)

mds = MDS(n_components=2, random_state=0)
X_2d = mds.fit_transform(df)

for final_feature in final_features:
    # Choosing a categorical column for color differentiation
    category = df[final_feature]

    # Generating a unique color for each category
    unique_categories = category.unique()
    palette = sns.color_palette("hsv", len(unique_categories))
    color_map = {cat: palette[i] for i, cat in enumerate(unique_categories)}

    # Plotting MDS results with color mapping
    plt.figure(figsize=(16, 12))
    for cat in unique_categories:
        indices = category == cat
        plt.scatter(X_2d[indices, 0], X_2d[indices, 1], label=cat, color=color_map[cat])

    plt.legend(loc="upper right")
    plt.xlabel("MDS axis 1")
    plt.ylabel("MDS axis 2")
    plt.title(f"{final_feature}")
    plt.show()
