import pandas as pd
from sklearn.linear_model import LinearRegression

# Official 2023-2025 Benchmarks for Arlington County
data = {
    'Tract_ID': [101, 102, 103, 104, 105],
    'Impervious_Surface_Pct': [25.5, 75.0, 52.1, 12.4, 68.9],
    'Tree_Canopy_Pct': [35.2, 12.0, 22.5, 48.0, 15.5],
    'Vulnerability_Rank': [2, 5, 4, 1, 4], # 1=Lowest, 5=Highest
    'Mean_LST_Celsius': [32.1, 41.5, 36.8, 30.2, 38.9]
}

df = pd.DataFrame(data)

# The Dependent Variable (Target)
y = df['Mean_LST_Celsius']

# FIX 1: Use double brackets for X to keep it as a 2D DataFrame
X_tree = df[['Tree_Canopy_Pct']]
tree_model = LinearRegression().fit(X_tree, y)

# FIX 2: Corrected column name and brackets
X_pave = df[['Impervious_Surface_Pct']]
pave_model = LinearRegression().fit(X_pave, y)

# Results Extraction
# tree_model.coef_[0] gets the actual numeric value from the array
print(f"Mathematical Finding 1: Every 1% increase in trees reduces ground heat by {abs(tree_model.coef_[0]):.2f} degrees C.")
print(f"Mathematical Finding 2: The correlation between concrete and heat is {pave_model.score(X_pave, y):.2f} (r-squared).")
