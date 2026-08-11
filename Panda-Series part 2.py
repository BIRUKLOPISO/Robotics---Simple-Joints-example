import pandas as pd
import numpy as np

print("=" * 60)
print("TOPIC 1: METHODS (head, tail, info, describe)")
print("=" * 60)

# Question 1
print("\n--- Question 1 ---")
data = pd.Series([15, 25, 35, 45, 55, 65, 75, 85, 95, 105,
                  np.nan, 125, np.nan, 145, 155], name="Scores")

print("Original Series:")
print(data)
print(f"\na) Number of non-null values: {data.count()}")
print(f"b) Data type: {data.dtype}")


# Question 2
print("\n--- Question 2 ---")
population = pd.Series([1200, 3400, 2800, 5600, 4900, 8100,
                        3700, 6300, np.nan, 7200], name="Population")

print("Population Statistics:")
stats = population.describe()
print(stats)


# Question 3
print("\n--- Question 3 ---")
months = pd.Series(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

print(f"head(6):\n{months.head(6)}")
print(f"\ntail(6):\n{months.tail(6)}")


# Question 4
print("\n--- Question 4 ---")
test_scores = pd.Series([88, 92, 75, 68, 94, 82, 79, 85, 91, 87])

print("head(3):")
print(test_scores.head(3))
print("\ntail(2):")
print(test_scores.tail(2))


# Question 5
print("\n--- Question 5 ---")
mixed_data = pd.Series([1, 'two', 3.0, 'four', 5, 6.5, 'seven', 8])

print("mixed_data info:")
print(f"Data type: {mixed_data.dtype}")

print("Reason: Mixed types (int, str, float) force object dtype")


print("\n" + "=" * 60)
print("TOPIC 2: HANDLING MISSING DATA (isna, dropna, fillna)")
print("=" * 60)

# Question 1
print("\n--- Question 1 ---")
data = pd.Series([15, np.nan, 25, np.nan, 35, 40, np.nan, 50, np.nan, 60])

missing_count = data.isna().sum()
print(f"Missing values count: {missing_count}")

# Question 2 - FIXED: New pandas syntax for forward fill
print("\n--- Question 2 ---")
scores = pd.Series([78, 92, np.nan, 85, np.nan, 88, 91, np.nan, 79, 94])

# FIX: Use method='ffill' is deprecated, use 'pad' or better: ffill()
ffill_filled = scores.ffill()  # New syntax
print("Forward fill result (using ffill()):")
print(ffill_filled)
print(f"\nIndex 2 value: {ffill_filled[2]} (should be 92.0)")
print(f"Index 8 value: {ffill_filled[8]} (should be 79.0)")



# Question 3 - FIXED: New pandas syntax for backward fill
print("\n--- Question 3 ---")
temperatures = pd.Series([22, 24, np.nan, 28, 30, np.nan, np.nan, 35, 32])

bfill_filled = temperatures.bfill()  # New syntax
print("Backward fill result (using bfill()):")
print(bfill_filled)
print(f"\na) Index 2: {bfill_filled[2]}  ")
print(f"b) Index 5: {bfill_filled[5]}  ")
print(f"c) Index 6: {bfill_filled[6]}  ")

# Question 4
print("\n--- Question 4 ---")
prices = pd.Series([10.99, 12.50, np.nan, 11.25, np.nan, 13.99, 14.50, np.nan])

mean_value = prices.mean()
filled_prices = prices.fillna(mean_value)

print(f"Mean of non-null values: {mean_value:.3f}")
print("Filled Series:")
print(filled_prices)


# Question 5
print("\n--- Question 5 ---")
print("Understanding inplace=True vs inplace=False")

data = pd.Series([5, np.nan, 10, np.nan, 15])
print(f"Original data ID: {id(data)}")
print("Original data:")
print(data)

# Operation A
result_a = data.fillna(0)
print(f"\nOperation A (new Series) ID: {id(result_a)}")
print("Result A:")
print(result_a)
print(f"Original data still same ID: {id(data)}")
print("Original data unchanged:")
print(data)

# Operation B
data.fillna(0, inplace=True)
print(f"\nOperation B (inplace) - original data MODIFIED")
print(f"Original data now has same ID but different content: {id(data)}")
print("Modified original:")
print(data)

print("\nKey insight:")
print("- Operation A: Creates NEW Series (safer, chainable)")
print("- Operation B: Modifies original (returns None, can't chain)")