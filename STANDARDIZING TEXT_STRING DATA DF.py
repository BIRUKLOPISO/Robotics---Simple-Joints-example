import pandas as pd
import numpy as np

print("=" * 60)
print("TOPIC 6: HANDLING OUTLIERS")
print("=" * 60)

# ============================================
# QUESTION 1: Employee Salary Analysis
# ============================================
print("\n" + "=" * 60)
print("QUESTION 1: Employee Salary Analysis")
print("=" * 60)

np.random.seed(42)
employee_data = pd.DataFrame({
    'employee_id': range(1, 51),
    'department': ['Sales', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'HR'] * 5,
    'salary': np.random.normal(60000, 10000, 50).astype(int),
    'bonus': np.random.normal(5000, 1500, 50).astype(int)
})

# Add intentional outliers
employee_data.loc[5, 'salary'] = 250000
employee_data.loc[12, 'salary'] = 8000
employee_data.loc[25, 'bonus'] = 50000
employee_data.loc[38, 'bonus'] = -10000

print("\nEmployee Data (first 10 rows):")
print(employee_data.head(10))
print(f"\nTotal rows: {len(employee_data)}")

# 1a - Detect salary outliers using IQR
Q1_salary = employee_data['salary'].quantile(0.25)
Q3_salary = employee_data['salary'].quantile(0.75)
IQR_salary = Q3_salary - Q1_salary
salary_lower = Q1_salary - 1.5 * IQR_salary
salary_upper = Q3_salary + 1.5 * IQR_salary
salary_outlier = (employee_data['salary'] < salary_lower) | (employee_data['salary'] > salary_upper)

print("\n1a. Salary outliers detected:")
print(f"Q1: ${Q1_salary:,.0f}")
print(f"Q3: ${Q3_salary:,.0f}")
print(f"IQR: ${IQR_salary:,.0f}")
print(f"Lower bound: ${salary_lower:,.0f}")
print(f"Upper bound: ${salary_upper:,.0f}")
print(f"Number of salary outliers: {salary_outlier.sum()}")
print(f"Outlier values: {employee_data.loc[salary_outlier, 'salary'].tolist()}")

# 1b - Detect bonus outliers using IQR
Q1_bonus = employee_data['bonus'].quantile(0.25)
Q3_bonus = employee_data['bonus'].quantile(0.75)
IQR_bonus = Q3_bonus - Q1_bonus
bonus_lower = Q1_bonus - 1.5 * IQR_bonus
bonus_upper = Q3_bonus + 1.5 * IQR_bonus
bonus_outlier = (employee_data['bonus'] < bonus_lower) | (employee_data['bonus'] > bonus_upper)

print("\n1b. Bonus outliers detected:")
print(f"Q1: ${Q1_bonus:,.0f}")
print(f"Q3: ${Q3_bonus:,.0f}")
print(f"IQR: ${IQR_bonus:,.0f}")
print(f"Lower bound: ${bonus_lower:,.0f}")
print(f"Upper bound: ${bonus_upper:,.0f}")
print(f"Number of bonus outliers: {bonus_outlier.sum()}")
print(f"Outlier values: {employee_data.loc[bonus_outlier, 'bonus'].tolist()}")

# 1c - Remove rows where either salary or bonus is an outlier
employee_data_clean = employee_data[~(salary_outlier | bonus_outlier)]

print("\n1c. After removing outliers:")
print(f"Original rows: {len(employee_data)}")
print(f"Rows after removing outliers: {len(employee_data_clean)}")
print(f"Rows removed: {len(employee_data) - len(employee_data_clean)}")

# 1d - Cap salary outliers
employee_data['salary_capped'] = employee_data['salary'].clip(lower=salary_lower, upper=salary_upper)

print("\n1d. Salary capped (original vs capped for outliers):")
print(employee_data[salary_outlier][['salary', 'salary_capped']])

# ============================================
# QUESTION 2: Product Price Analysis by Category
# ============================================
print("\n" + "=" * 60)
print("QUESTION 2: Product Price Analysis by Category")
print("=" * 60)

np.random.seed(123)
products = pd.DataFrame({
    'product_id': range(1, 101),
    'category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Home', 'Electronics', 'Home', 'Clothing', 'Electronics', 'Home'] * 10,
    'price': np.random.normal(100, 30, 100).astype(int),
    'rating': np.random.uniform(1, 5, 100).round(1)
})

# Add outliers
products.loc[3, 'price'] = 1000
products.loc[18, 'price'] = 5
products.loc[42, 'rating'] = 0
products.loc[89, 'price'] = 800

print("\nProduct Data (first 10 rows):")
print(products.head(10))
print(f"\nTotal rows: {len(products)}")

# 2a - Create function to detect outliers
def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (df[column] < lower_bound) | (df[column] > upper_bound)

# 2b - Detect outliers in price and rating
price_outliers = detect_outliers_iqr(products, 'price')
rating_outliers = detect_outliers_iqr(products, 'rating')

print("\n2b. Outlier detection:")
print(f"Price outliers: {price_outliers.sum()}")
print(f"Rating outliers: {rating_outliers.sum()}")
print("Note: IQR may not be appropriate for rating (bounded 1-5)")

# 2c - Category-specific outlier detection
products['Q1_by_cat'] = products.groupby('category')['price'].transform(lambda x: x.quantile(0.25))
products['Q3_by_cat'] = products.groupby('category')['price'].transform(lambda x: x.quantile(0.75))
products['IQR_by_cat'] = products['Q3_by_cat'] - products['Q1_by_cat']
products['lower_bound'] = products['Q1_by_cat'] - 1.5 * products['IQR_by_cat']
products['upper_bound'] = products['Q3_by_cat'] + 1.5 * products['IQR_by_cat']
products['price_outlier_by_category'] = (products['price'] < products['lower_bound']) | (products['price'] > products['upper_bound'])

print("\n2c. Category-specific outliers:")
print(products[products['price_outlier_by_category']][['category', 'price', 'Q1_by_cat', 'Q3_by_cat', 'lower_bound', 'upper_bound']])

# 2d - Remove category-specific outliers and compare statistics
original_stats = products.groupby('category')['price'].agg(['mean', 'median'])
cleaned_products = products[~products['price_outlier_by_category']]
rows_removed = len(products) - len(cleaned_products)
new_stats = cleaned_products.groupby('category')['price'].agg(['mean', 'median'])
comparison = new_stats - original_stats

print("\n2d. After removing category-specific outliers:")
print(f"Rows removed: {rows_removed}")
print("\nOriginal means and medians by category:")
print(original_stats)
print("\nNew means and medians by category:")
print(new_stats)
print("\nDifference (New - Original):")
print(comparison)

# ============================================
# QUESTION 3: Student Test Scores with Multiple Subjects
# ============================================
print("\n" + "=" * 60)
print("QUESTION 3: Student Test Scores with Multiple Subjects")
print("=" * 60)

np.random.seed(789)
students = pd.DataFrame({
    'student_id': range(1, 81),
    'class': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'] * 8,
    'math_score': np.random.normal(75, 15, 80).astype(int),
    'science_score': np.random.normal(70, 12, 80).astype(int),
    'english_score': np.random.normal(80, 10, 80).astype(int)
})

# Add various outliers
students.loc[7, 'math_score'] = 15
students.loc[14, 'science_score'] = 98
students.loc[23, 'english_score'] = 35
students.loc[31, 'math_score'] = 100
students.loc[45, 'science_score'] = 45
students.loc[56, 'english_score'] = 95
students.loc[62, 'math_score'] = 8
students.loc[73, 'science_score'] = 100
students.loc[78, 'math_score'] = 0

print("\nStudent Data (first 10 rows):")
print(students.head(10))
print(f"\nTotal students: {len(students)}")

# 3a - Detect outliers for each subject
def get_outlier_info(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = (df[column] < lower) | (df[column] > upper)
    return {
        'column': column,
        'lower_bound': lower,
        'upper_bound': upper,
        'count': outliers.sum(),
        'outlier_values': df.loc[outliers, column].tolist()
    }

print("\n3a. Outlier summary by subject:")
for subject in ['math_score', 'science_score', 'english_score']:
    info = get_outlier_info(students, subject)
    print(f"\n{subject}:")
    print(f"  Lower bound: {info['lower_bound']:.1f}")
    print(f"  Upper bound: {info['upper_bound']:.1f}")
    print(f"  Number of outliers: {info['count']}")
    print(f"  Outlier values: {info['outlier_values']}")

# 3b - Create columns for any_outlier and outlier_count
math_outliers = detect_outliers_iqr(students, 'math_score')
science_outliers = detect_outliers_iqr(students, 'science_score')
english_outliers = detect_outliers_iqr(students, 'english_score')

students['any_outlier'] = math_outliers | science_outliers | english_outliers
students['outlier_count'] = math_outliers.astype(int) + science_outliers.astype(int) + english_outliers.astype(int)

print("\n3b. Outlier summary per student:")
print(students[['student_id', 'outlier_count', 'any_outlier']].head(10))

# 3c - Remove students with outliers in 2 or more subjects
students_clean = students[students['outlier_count'] < 2]

original_means = students[['math_score', 'science_score', 'english_score']].mean()
new_means = students_clean[['math_score', 'science_score', 'english_score']].mean()

print("\n3c. After removing students with 2+ subject outliers:")
print(f"Original rows: {len(students)}")
print(f"Rows after removal: {len(students_clean)}")
print(f"Rows removed: {len(students) - len(students_clean)}")
print("\nOriginal means:")
print(original_means)
print("\nNew means:")
print(new_means)
print("\nDifference:")
print(new_means - original_means)

# 3d - Impute outliers with class median
students_imputed = students.copy()
for subject in ['math_score', 'science_score', 'english_score']:
    students_imputed[subject] = students_imputed.groupby('class')[subject].transform(
        lambda x: x.mask(detect_outliers_iqr(students_imputed, subject), x.median())
    )

print("\n3d. After imputing outliers with class median:")
print(f"Number of outliers fixed: {students_imputed['outlier_count'].sum()}")
print(f"Mean difference after imputation:")
print(students_imputed[['math_score', 'science_score', 'english_score']].mean() - original_means)

print("\n" + "=" * 60)
print("END OF TOPIC 6")
print("=" * 60)