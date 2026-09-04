import pandas as pd
import numpy as np
import time

print("=" * 60)
print("TOPIC 14: WORKING WITH LARGE DATASETS (PERFORMANCE)")
print("=" * 60)

# ============================================
# CREATE LARGE DATASET (100,000 rows)
# ============================================
print("\n" + "=" * 60)
print("CREATING LARGE DATASET")
print("=" * 60)

np.random.seed(42)
large_data = pd.DataFrame({
    'id': range(1, 100001),
    'age': np.random.randint(18, 70, 100000),
    'salary': np.random.randint(30000, 80000, 100000),
    'department': np.random.choice(['Sales', 'IT', 'HR', 'Finance', 'Marketing'], 100000),
    'status': np.random.choice(['Active', 'Inactive', 'Pending'], 100000),
    'score': np.random.uniform(0, 100, 100000)
})

print("\nLarge Dataset Created!")
print(f"Shape: {large_data.shape}")
print(f"Memory usage: {large_data.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# ============================================
# QUESTION 14a: Check Memory Usage
# ============================================
print("\n" + "=" * 60)
print("QUESTION 14a: Check Memory Usage")
print("=" * 60)

before = large_data.memory_usage(deep=True).sum() / 1024**2
print(f"Before optimization: {before:.2f} MB")

# ============================================
# QUESTION 14b: Optimize Data Types
# ============================================
print("\n" + "=" * 60)
print("QUESTION 14b: Optimize Data Types")
print("=" * 60)

large_data["age"] = large_data["age"].astype('int32')
large_data["salary"] = large_data["salary"].astype('float32')
large_data[["department", "status"]] = large_data[["department", "status"]].astype('category')
large_data["score"] = large_data["score"].astype('float32')

print("Optimization complete!")
print(large_data.dtypes)

# ============================================
# QUESTION 14c: Check Memory After Optimization
# ============================================
print("\n" + "=" * 60)
print("QUESTION 14c: Memory After Optimization")
print("=" * 60)

after = large_data.memory_usage(deep=True).sum() / 1024**2
saved = before - after
saved_percent = (saved / before) * 100

print(f"Before optimization: {before:.2f} MB")
print(f"After optimization: {after:.2f} MB")
print(f"Memory saved: {saved:.2f} MB ({saved_percent:.1f}%)")

# ============================================
# QUESTION 14d: Filter with query() - Age, Salary, Department
# ============================================
print("\n" + "=" * 60)
print("QUESTION 14d: Filter with query() - Age, Salary, Department")
print("=" * 60)

filtered_d = large_data.query("age > 25 and age < 40 and salary > 50000 and (department == 'IT' or department == 'Sales')")
print(f"Filtered rows: {len(filtered_d)}")
print(filtered_d.head())

# ============================================
# QUESTION 14e: Filter with query() - Status and Score
# ============================================
print("\n" + "=" * 60)
print("QUESTION 14e: Filter with query() - Status and Score")
print("=" * 60)

filtered_e = large_data.query("status == 'Active' and score > 60 and score < 90")
print(f"Filtered rows: {len(filtered_e)}")
print(filtered_e.head())

# ============================================
# QUESTION 14f: Compare query() vs Boolean Indexing Performance
# ============================================
print("\n" + "=" * 60)
print("QUESTION 14f: Performance Comparison - query() vs Boolean Indexing")
print("=" * 60)

# Boolean Indexing
start = time.time()
result1 = large_data[
    (large_data['age'] > 25) & (large_data['age'] < 40) &
    (large_data['salary'] > 50000) &
    ((large_data['department'] == 'IT') | (large_data['department'] == 'Sales'))
]
end = time.time()
bool_time = end - start
print(f"Boolean indexing time: {bool_time:.4f} seconds")
print(f"Result shape: {result1.shape}")

# Query() method
start = time.time()
result2 = large_data.query("age > 25 and age < 40 and salary > 50000 and (department == 'IT' or department == 'Sales')")
end = time.time()
query_time = end - start
print(f"Query() time: {query_time:.4f} seconds")
print(f"Result shape: {result2.shape}")

# Compare results
print(f"\nResults match: {result1.shape == result2.shape}")
if bool_time < query_time:
    print(f"Boolean indexing was faster by {query_time - bool_time:.4f} seconds")
else:
    print(f"Query() was faster by {bool_time - query_time:.4f} seconds")
