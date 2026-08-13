import pandas as pd
import numpy as np

print("=" * 60)
print("TOPIC 5: FILTERING & BOOLEAN INDEXING")
print("=" * 60)

# Create sample data for filtering questions - using FLOAT to allow decimal values
sales = pd.Series([150.0, 225.0, 98.0, 450.0, 275.0, 325.0, 175.0, 210.0, 95.0, 400.0,
                   180.0, 250.0, 125.0, 350.0, 300.0, 275.0, 450.0, 190.0, 215.0, 380.0],
                  name="Daily_Sales")

print("\n=== FILTERING PRACTICE ===")
print("Original Sales Data (first 10):")
print(sales.head(10))

# Question 1: Basic filtering
print("\n--- Question 1: Basic Filtering ---")
high_sales = sales[sales > 300]
print(f"Sales > 300: {high_sales.tolist()}")

# Question 2: Multiple conditions (AND)
print("\n--- Question 2: AND Conditions ---")
mid_sales = sales[(sales >= 200) & (sales <= 300)]
print(f"Sales between 200-300: {mid_sales.tolist()}")

# Question 3: Multiple conditions (OR)
print("\n--- Question 3: OR Conditions ---")
extreme_sales = sales[(sales < 100) | (sales > 400)]
print(f"Sales <100 OR >400: {extreme_sales.tolist()}")

# Question 4: isin() method
print("\n--- Question 4: isin() Method ---")
specific_values = sales[sales.isin([175, 225, 275, 325])]
print(f"Sales matching [175,225,275,325]: {specific_values.tolist()}")

# Question 5: between() method
print("\n--- Question 5: between() Method ---")
print(f"Sales between 200-300 (using between): {sales[sales.between(200, 300)].tolist()}")

# Question 6: String filtering
print("\n--- Question 6: String Filtering ---")
names = pd.Series(['Alice', 'Bob', 'Charlie', 'David', 'Eve',
                   'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'])

a_names = names[names.str.startswith('A')]
print(f"Names starting with 'A': {a_names.tolist()}")

names_with_e = names[names.str.contains('e', case=False)]
print(f"Names containing 'e': {names_with_e.tolist()}")

# Question 7: Missing data filtering
print("\n--- Question 7: Missing Data Filtering ---")
data_with_nan = pd.Series([10, 20, np.nan, 30, np.nan, 40, 50, np.nan])

print(f"Missing values: {data_with_nan[data_with_nan.isna()].tolist()}")
print(f"Non-missing values: {data_with_nan[data_with_nan.notna()].tolist()}")

# Question 8: Complex filtering
print("\n--- Question 8: Complex Filtering ---")
avg_sales = sales.mean()
excluded = [175, 225, 275]

complex_filter = sales[(sales > avg_sales) &
                       (~sales.isin(excluded)) &
                       (sales.notna())]
print(f"Sales > average, not in excluded, not missing: {complex_filter.tolist()}")

# Question 9: Modifying with filters - FIXED VERSION
print("\n--- Question 9: Modifying Filtered Data ---")
sales_copy = sales.copy()
print("Original first 5:", sales_copy.head().tolist())

# FIX: Convert to float first or ensure we're working with float
sales_copy = sales_copy.astype(float)  # Ensure float type
# Apply 10% bonus to sales under 200
mask = sales_copy < 200
sales_copy[mask] = sales_copy[mask] * 1.1
print("After bonus (first 5):", [round(x, 2) for x in sales_copy.head().tolist()])

# Alternative FIX: Round to integers if you want to keep ints
print("\nAlternative (keeping integers):")
sales_copy2 = sales.copy().astype(float)
mask = sales_copy2 < 200
sales_copy2[mask] = (sales_copy2[mask] * 1.1).round(0)  # Round to nearest integer
print("After bonus (rounded to ints):", sales_copy2.head().tolist())

# Question 10: Percentile-based filtering
print("\n--- Question 10: Percentile Filtering ---")
threshold = sales.quantile(0.8)
top_performers = sales[sales >= threshold]
print(f"Top 20% threshold: {threshold}")
print(f"Top performers: {top_performers.tolist()}")