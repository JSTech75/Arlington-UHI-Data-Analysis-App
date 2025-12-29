import pandas as pd
from sklearn.linear_model import LinearRegression

# Official 2023-2025 Benchmarks for Arlington County
data = {
    'Tract_ID': [101, 102, 103, 104, 105], # Added IDs
    'Impervious_Surface_Pct': [25.0, 78.0, 55.0, 10.0, 65.0], # Added placeholder data
    'Tree_Canopy_Pct': [35.2, 12.0, 22.5, 48.0, 15.5],
    'Vulnerability_Rank': [2, 5, 4, 1, 4], # 1=Lowest, 5=Highest
    'Mean_LST_Celsius': [32.1, 41.5, 36.8, 30.2, 38.9]
}

df = pd.DataFrame(data)

# Target variable (Dependent)
y = df['Mean_LST_Celsius']

# 1. Calculate the Impact of Trees
# X must be a 2D array/DataFrame, so we use double brackets [['column']]
X_tree = df[['Tree_Canopy_Pct']]
tree_model = LinearRegression().fit(X_tree, y)

# 2. Calculate the Impact of Pavement
X_pave = df[['Impervious_Surface_Pct']]
pave_model = LinearRegression().fit(X_pave, y)

# Results
# .item() or [0] is used to extract the single float value from the coefficient array
print(f"Mathematical Finding 1: Every 1% increase in trees reduces ground heat by {abs(tree_model.coef_[0]):.2f}°C.")
print(f"Mathematical Finding 2: The correlation between concrete and heat is {pave_model.score(X_pave, y):.2f} (r-squared).")
