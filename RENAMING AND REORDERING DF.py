import pandas as pd

print("=" * 60)
print("TOPIC 8: RENAMING AND REORDERING")
print("=" * 60)

# ============================================
# QUESTION 1: Employee Data - Renaming and Reordering
# ============================================
print("\n" + "=" * 60)
print("QUESTION 1: Employee Data - Renaming and Reordering")
print("=" * 60)

employee_data = pd.DataFrame({
    'emp_id': [101, 102, 103, 104, 105],
    'emp_first': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'emp_last': ['Smith', 'Jones', 'Brown', 'Lee', 'Wong'],
    'emp_salary': [60000, 55000, 65000, 52000, 58000],
    'emp_dept': ['Sales', 'IT', 'Sales', 'HR', 'IT'],
    'emp_city': ['NYC', 'LA', 'Chicago', 'NYC', 'LA']
})

print("\nOriginal DataFrame:")
print(employee_data)
print(f"\nColumns: {employee_data.columns.tolist()}")

# 1a - Rename columns
renamed = employee_data.rename(columns={
    'emp_id': 'ID',
    'emp_first': 'First Name',
    'emp_last': 'Last Name',
    'emp_salary': 'Salary',
    'emp_dept': 'Department',
    'emp_city': 'City'
})

print("\n1a. After renaming columns:")
print(renamed)

# 1b - Reorder columns
re_indexed = renamed.reindex(columns=['ID', 'First Name', 'Last Name', 'Department', 'City', 'Salary'])

print("\n1b. After reordering columns:")
print(re_indexed)

# 1c - Drop City column
print("\n1c. After dropping City column:")
print(re_indexed.drop(columns=['City']))

# ============================================
# QUESTION 2: Product Inventory - Multiple Operations
# ============================================
print("\n" + "=" * 60)
print("QUESTION 2: Product Inventory - Multiple Operations")
print("=" * 60)

product_data = pd.DataFrame({
    'prod_code': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'USB Cable'],
    'price': [999.99, 25.50, 75.00, 199.00, 12.75],
    'stock_qty': [50, 200, 150, 30, 500],
    'supplier_info': ['Supplier A', 'Supplier B', 'Supplier A', 'Supplier C', 'Supplier B'],
    'warehouse_id': ['WH1', 'WH2', 'WH1', 'WH3', 'WH2']
})

print("\nOriginal DataFrame:")
print(product_data)
print(f"\nColumns: {product_data.columns.tolist()}")

# 2a - Rename columns
re_named = product_data.rename(columns={
    'prod_code': 'Product ID',
    'product_name': 'Name',
    'price': 'Price',
    'stock_qty': 'Stock',
    'supplier_info': 'Supplier',
    'warehouse_id': 'Warehouse'
})

print("\n2a. After renaming columns:")
print(re_named)

# 2b - Reorder columns
re_indexed = re_named.reindex(columns=['Product ID', 'Name', 'Price', 'Stock', 'Supplier', 'Warehouse'])

print("\n2b. After reordering columns:")
print(re_indexed)

# 2c - Rename index labels
column_re_indexed = re_indexed.rename(index={0: 'Row1', 1: 'Row2', 2: 'Row3', 3: 'Row4', 4: 'Row5'})

print("\n2c. After renaming index:")
print(column_re_indexed)

# ============================================
# QUESTION 3: Student Grades - Uncovered Concepts
# ============================================
print("\n" + "=" * 60)
print("QUESTION 3: Student Grades - Uncovered Concepts")
print("=" * 60)

student_data = pd.DataFrame({
    'StudentID': [201, 202, 203, 204, 205],
    'FirstName': ['John', 'Sarah', 'Mike', 'Emily', 'David'],
    'LastName': ['Smith', 'Jones', 'Brown', 'Lee', 'Wong'],
    'Math_Score': [85, 90, 78, 92, 88],
    'Science_Score': [88, 85, 92, 79, 90],
    'English_Score': [78, 88, 85, 90, 92],
    'Grade_Level': ['Freshman', 'Sophomore', 'Junior', 'Senior', 'Freshman']
})

print("\nOriginal DataFrame:")
print(student_data)
print(f"\nColumns: {student_data.columns.tolist()}")

# 3a - Rename columns to uppercase using inplace=True
student_data.rename(columns=str.upper, inplace=True)
print("\n3a. After renaming to uppercase:")
print(student_data.columns.tolist())

# 3b - Move 'GRADE_LEVEL' to front
def move_columns(df, col, position):
    columns = df.columns.tolist()
    columns.remove(col)
    columns.insert(position, col)
    return df[columns]

student_data = move_columns(student_data, 'GRADE_LEVEL', 0)
print("\n3b. After moving GRADE_LEVEL to front:")
print(student_data.head())

# 3c - Drop rows with index 1 and 3
dropped = student_data.drop(index=[1, 3])
print("\n3c. After dropping rows 1 and 3:")
print(dropped)

# 3d - Drop LASTNAME column
dropped = dropped.drop(columns='LASTNAME')
print("\n3d. After dropping LASTNAME column:")
print(dropped)