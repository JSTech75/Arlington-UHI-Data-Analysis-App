import pandas as pd
from sklearn.linear_model import LinearRegression

# Official 2023-2025 Benchmarks for Arlington County
# data based on 2023 Tree Assessment and 2025 CVIM rankings
data = {
    'Tract_ID': ,
    'Impervious_Surface_Pct': ,
    'Tree_Canopy_Pct': [35.2, 12.0, 22.5, 48.0, 15.5],
    'Vulnerability_Rank': [2, 5, 4, 1, 4], # 1=Lowest, 5=Highest
    'Mean_LST_Celsius': [32.1, 41.5, 36.8, 30.2, 38.9]
}

df = pd.DataFrame(data)

# Calculate the Impact of Trees (Independent Variable: Canopy, Dependent: LST)
x = df]
y = df
tree_model = LinearRegression().fit(X, y)

# Calculate the Impact of Pavement (Independent Variable: Impervious, Dependent: LST)
X_pave = df]
pave_model = LinearRegression().fit(X_pave, y)

print(f"Mathematical Finding 1: Every 1% increase in trees reduces ground heat by {abs(tree_model.coef_):.2f} degrees C.")
print(f"Mathematical Finding 2: The correlation between concrete and heat is {pave_model.score(X_pave, y):.2f} (r-squared).")
