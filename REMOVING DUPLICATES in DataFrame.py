import pandas as pd

print("=" * 60)
print("TOPIC 3: REMOVING DUPLICATES")
print("=" * 60)

# ============================================
# QUESTION 1: Customer Database with Duplicate Emails
# ============================================
print("\n" + "=" * 60)
print("QUESTION 1: Customer Database with Duplicate Emails")
print("=" * 60)

customers = pd.DataFrame({
    'customer_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    'email': ['john@gmail.com', 'sarah@yahoo.com', 'john@gmail.com', 'mike@hotmail.com', 'sarah@yahoo.com', 'john@gmail.com', 'lisa@gmail.com'],
    'signup_date': ['2024-01-15', '2024-01-20', '2024-01-25', '2024-02-01', '2024-02-10', '2024-02-15', '2024-02-20'],
    'total_purchases': [5, 3, 2, 7, 4, 1, 6]
})

print("\nOriginal Customer Data:")
print(customers)

# 1a - Identify duplicate emails
print("\n1a. Duplicate emails (boolean mask):")
print(customers.duplicated(subset=['email']))

# 1b - Display duplicate email records
print("\n1b. Duplicate email records (showing extra copies):")
dup_email = customers.duplicated(subset=['email'])
print(customers[dup_email])

# 1c - Remove duplicates keeping last occurrence
print("\n1c. After removing duplicates (keeping last):")
print(customers.drop_duplicates(subset=['email'], keep='last'))

# 1d - Remove duplicates and reset index
print("\n1d. After removing duplicates and resetting index:")
print(customers.drop_duplicates(subset=['email']).reset_index(drop=True))

# ============================================
# QUESTION 2: Sales Data with Complete Row Duplicates
# ============================================
print("\n" + "=" * 60)
print("QUESTION 2: Sales Data with Complete Row Duplicates")
print("=" * 60)

sales = pd.DataFrame({
    'date': ['2024-05-01', '2024-05-01', '2024-05-02', '2024-05-02', '2024-05-03', '2024-05-01', '2024-05-03'],
    'product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Laptop', 'Mouse'],
    'quantity': [1, 2, 1, 1, 2, 1, 2],
    'price': [1000, 25, 1000, 50, 25, 1000, 25]
})

print("\nOriginal Sales Data:")
print(sales)

# 2a - Check for complete duplicates
print("\n2a. Complete row duplicates (boolean mask):")
print(sales.duplicated())

# 2b - Count duplicate rows
print("\n2b. Number of duplicate rows:")
print(sales.duplicated().sum())

# 2c - Remove ALL duplicates (keep only unique rows)
print("\n2c. After removing ALL duplicates (keeping only unique rows):")
dro = sales.duplicated()
print(sales[~dro])

# 2d - Show which rows were removed
print("\n2d. Removal mask (True = removed):")
print(sales.duplicated())

# ============================================
# QUESTION 3: Employee Timecards - Finding Duplicate Date Entries
# ============================================
print("\n" + "=" * 60)
print("QUESTION 3: Employee Timecards - Finding Duplicate Date Entries")
print("=" * 60)

timecards = pd.DataFrame({
    'employee_id': [101, 101, 102, 103, 101, 102, 103, 101, 104],
    'date': ['2024-06-01', '2024-06-01', '2024-06-01', '2024-06-01',
             '2024-06-02', '2024-06-02', '2024-06-02', '2024-06-01', '2024-06-01'],
    'hours_worked': [8, 8, 7, 8, 8, 7, 8, 8, 6],
    'department': ['Sales', 'Sales', 'IT', 'HR', 'Sales', 'IT', 'HR', 'Sales', 'Marketing']
})

print("\nOriginal Timecard Data:")
print(timecards)

# 3a - Find duplicates by employee_id and date
print("\n3a. Duplicate entries (same employee on same date):")
dup = timecards.duplicated(['employee_id', 'date'])
print(timecards[dup])

# 3b - Count duplicates for employee 101 on June 1st
print("\n3b. Number of duplicate entries for employee 101 on June 1st:")
print(timecards.duplicated(['employee_id', 'date']).sum())

# 3c - Remove duplicates keeping first occurrence
print("\n3c. After removing duplicates (keeping first):")
print(timecards.drop_duplicates())

# 3d - Verify employee 101 has only one entry for June 1st
print("\n3d. Verify employee 101 on 2024-06-01 (after cleaning):")
chc = timecards.drop_duplicates()
print(chc[(chc['employee_id'] == 101) & (chc['date'] == '2024-06-01')])

# ============================================
# QUESTION 4: Product Inventory - Complex Duplicate Detection
# ============================================
print("\n" + "=" * 60)
print("QUESTION 4: Product Inventory - Complex Duplicate Detection")
print("=" * 60)

inventory = pd.DataFrame({
    'product_code': ['P001', 'P002', 'P003', 'P001', 'P004', 'P002', 'P001', 'P005', 'P003'],
    'supplier': ['Supplier A', 'Supplier B', 'Supplier A', 'Supplier A', 'Supplier C', 'Supplier B', 'Supplier D', 'Supplier A', 'Supplier A'],
    'warehouse': ['WH1', 'WH2', 'WH1', 'WH1', 'WH3', 'WH2', 'WH1', 'WH4', 'WH1'],
    'stock': [100, 50, 75, 100, 200, 55, 100, 30, 80],
    'last_updated': ['2024-05-01', '2024-05-01', '2024-05-02', '2024-05-10',
                     '2024-05-01', '2024-05-15', '2024-05-20', '2024-05-01', '2024-05-25']
})

print("\nOriginal Inventory Data:")
print(inventory)

# 4a - Find products that appear more than once from same supplier
print("\n4a. Duplicate product-supplier combinations:")
dup = inventory.duplicated(subset=['product_code', 'supplier'])
print(inventory[dup])

# 4b - For product P001, mark all except most recent as duplicates
print("\n4b. P001 duplicate mask (True = duplicate, keeping most recent):")
p001_mask = inventory['product_code'] == 'P001'
most_recent_idx = inventory[p001_mask]['last_updated'].idxmax()
dup_mask = p001_mask & (inventory.index != most_recent_idx)
print(dup_mask)

# 4c - Remove duplicates keeping highest stock
print("\n4c. After removing duplicates (keeping highest stock):")
cleaned = inventory.sort_values('stock', ascending=False).drop_duplicates(subset=['product_code', 'supplier'])
print(cleaned)

# 4d - Count unique product-supplier pairs remaining
print("\n4d. Number of unique product-supplier pairs remaining:")
print(len(cleaned))

