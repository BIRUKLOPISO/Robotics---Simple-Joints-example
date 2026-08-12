import pandas as pd
import numpy as np

print("=" * 60)
print("TOPIC 3: STATISTICAL METHODS (mean, median, mode, std, etc.)")
print("=" * 60)

# Question 1
print("\n--- Question 1 ---")
ages = pd.Series([25, 32, 28, 35, 40, 29, 33, 31, 27, 36,
                  38, 42, 29, 31, np.nan, 34, 37, 41, 30, 33])

print("Age Data Statistics:")
print(f"Mean: {ages.mean():.6f}")
print(f"Median: {ages.median()}")
print(f"Mode: {ages.mode().tolist()}")


# Question 2
print("\n--- Question 2 ---")
salaries = pd.Series([45000, 52000, 48000, 95000, 51000, 47000,
                      53000, 49000, 175000, 50000, 51500, 48500])

mean_sal = salaries.mean()
median_sal = salaries.median()
Q1 = salaries.quantile(0.25)
Q3 = salaries.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = salaries[(salaries < lower_bound) | (salaries > upper_bound)]

print(f"Mean salary: ${mean_sal:,.0f}")
print(f"Median salary: ${median_sal:,.0f}")
print(f"\nWhich is more representative? The MEDIAN (${median_sal:,.0f})")
print("Because the mean (${mean_sal:,.0f}) is pulled up by outlier: $175,000")
print(f"\nOutliers using IQR method: {outliers.tolist()}")

# Question 3
print("\n--- Question 3 ---")
temperatures = pd.Series([72, 68, 74, 71, 69, 73, 75, 70, 72, 71,
                          68, 74, 73, 72, 71, 70, 69, 72, 74, 73])

temp_range = temperatures.max() - temperatures.min()
temp_std = temperatures.std()
temp_90th = temperatures.quantile(0.9)

print(f"a) Range: {temperatures.max()} - {temperatures.min()} = {temp_range} ")
print(f"b) Standard Deviation: {temp_std} ")
print(f"c) 90th Percentile: {temp_90th} ")

# Question 4
print("\n--- Question 4 ---")
dataset_a = pd.Series([10, 12, 11, 13, 12, 11, 10, 12, 13, 11])
dataset_b = pd.Series([5, 25, 10, 30, 15, 20, 5, 35, 10, 25])

std_a = dataset_a.std()
std_b = dataset_b.std()

print(f"Dataset A std: {std_a}")
print(f"Dataset B std: {std_b}")
print(f"\nDataset B has higher standard deviation ({std_b:.2f} vs {std_a:.2f})")
print("Because values are more spread out (5 to 35 vs 10 to 13) ✓")

# Question 5
print("\n--- Question 5 ---")
sales_data = pd.Series([100, 150, 200, np.nan, 175, 225, np.nan,
                        250, 300, 275, 325, np.nan, 350, 375, 400])

print(f"a) Mean (skipna=True): {sales_data.mean()} ")
print(f"b) Mean (skipna=False): {sales_data.mean(skipna=False)} ")
print(f"c) Sum: {sales_data.sum()} ")
print(f"   (12 non-null values sum to 3,125)")


print("\n" + "=" * 60)
print("TOPIC 4: VALUE COUNTING & UNIQUE VALUES")
print("=" * 60)

# Question 1
print("\n--- Question 1 ---")
fruits = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana',
                    'apple', 'grape', 'banana', 'apple', 'mango',
                    'banana', 'apple', 'orange', 'banana', np.nan])

unique_count = fruits.nunique()
value_counts = fruits.value_counts()
apple_count = value_counts.get('apple', 0)
total_with_nan = len(fruits)
apple_pct = (apple_count / total_with_nan) * 100

print(f"a) Unique fruit types (excluding NaN): {unique_count} ")
print(f"b) Most common fruits: Apple ({value_counts['apple']}) and Banana ({value_counts['banana']}) ")
print(f"c) Percentage of apples (including NaN): {apple_pct:.2f}% ")

# Question 2
print("\n--- Question 2 ---")
survey = pd.Series(['Yes', 'No', 'Yes', 'No', 'Yes', 'Maybe',
                    'Yes', 'No', 'Yes', 'No', 'Undecided', 'Yes',
                    'No', 'Yes', 'No', 'Maybe', 'Yes', np.nan])

print("a) Including NaN:")
print(survey.value_counts(dropna=False))
print("\nb) Proportions (excluding NaN):")
print(survey.value_counts(normalize=True))

rare = survey.value_counts()[survey.value_counts() < 3]
print(f"\nc) Responses appearing < 3 times:")
print(rare)
print("Your answers: Maybe(2), Undecided(1) ✓")

# Question 3
print("\n--- Question 3 ---")
data = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

print(f"unique(): {data.unique()} ✓")
print(f"nunique(): {data.nunique()} ✓")
print(f"value_counts().head(2):")
print(data.value_counts().head(2))


# Question 4
print("\n--- Question 4 ---")
grades = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'F', 'B',
                    'A', 'D', 'C', 'B', 'A', 'B', 'C'])

print("a) Grade distribution as percentages:")
grade_pct = (grades.value_counts(normalize=True) * 100).sort_index()
for grade, pct in grade_pct.items():
    print(f"   {grade}: {pct:.2f}%")

print("\nb) Grades appearing at least 3 times:")
grade_counts = grades.value_counts()
freq_grades = grade_counts[grade_counts >= 3]
print(freq_grades)

mode_value = grades.mode()
print(f"\nc) Mode(s): {mode_value.tolist()} ✓")
print("   (A appears 5 times, B appears 4 times, C appears 3 times)")

# Question 5
print("\n--- Question 5 ---")
responses = pd.Series(['Cat', 'Dog', 'Dog', 'Fish', 'Cat', 'Bird',
                       'Dog', 'Cat', 'Hamster', 'Dog', 'Cat', np.nan])

counts = responses.value_counts()
rare_pets = counts[counts < 2]

print("Values appearing less than twice:")
print(rare_pets)