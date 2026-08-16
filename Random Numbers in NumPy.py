import numpy as np

print("=" * 60)
print("NUMPY RANDOM - COMPLETE PRACTICE (ALL CONCEPTS)")
print("=" * 60)

# ============================================================
print("\n" + "=" * 60)
print("CONCEPT 1: rand - Uniform Distribution [0, 1)")
print("=" * 60)

# Example
print("\nExample 1: 5 random numbers between 0 and 1")
print(np.random.rand(5))

print("\nExample 2: 2x3 matrix of random numbers between 0 and 1")
print(np.random.rand(2, 3))


print("\n" + "-" * 40)
print("YOUR ANSWERS:")
print("Task 1: 1D array with 7 random numbers")
print(np.random.rand(7))

print("\nTask 2: 3x4 matrix of random numbers")
print(np.random.rand(3, 4))

# ============================================================
print("\n" + "=" * 60)
print("CONCEPT 2: randint - Random Integers")
print("=" * 60)

# Example
print("\nExample 1: 5 random integers between 1 and 10")
print(np.random.randint(1, 10, 5))

print("\nExample 2: 2x3 matrix of integers between 5 and 20")
print(np.random.randint(5, 20, (2, 3)))


print("\n" + "-" * 40)
print("YOUR ANSWERS:")
print("Task 1: 8 random integers between 10 and 20")
print(np.random.randint(10, 20, 8))

print("\nTask 2: 4x5 matrix of integers between 50 and 100")
print(np.random.randint(50, 100, (4, 5)))

# ============================================================
print("\n" + "=" * 60)
print("CONCEPT 3: randn - Standard Normal Distribution (mean=0, std=1)")
print("=" * 60)


print("\nExample 1: 5 numbers from standard normal")
print(np.random.randn(5))

print("\nExample 2: 2x3 matrix from standard normal")
print(np.random.randn(2, 3))


print("\n" + "-" * 40)
print("YOUR ANSWERS:")
print("Task 1: 6 numbers from standard normal")
print(np.random.randn(6))

print("\nTask 2: 3x3 matrix from standard normal")
print(np.random.randn(3, 3))

# ============================================================
print("\n" + "=" * 60)
print("CONCEPT 4: uniform - Custom Range Uniform Distribution")
print("=" * 60)

# Example
print("\nExample 1: 5 numbers between 2 and 5")
print(np.random.uniform(2, 5, 5))

print("\nExample 2: 2x3 matrix between -10 and 10")
print(np.random.uniform(-10, 10, (2, 3)))


print("\n" + "-" * 40)
print("YOUR ANSWERS:")
print("Task 1: 10 numbers between 5 and 15")
print(np.random.uniform(5, 15, 10))

print("\nTask 2: 4x2 matrix between -5 and 5")
print(np.random.uniform(-5, 5, (4, 2)))

# ============================================================
print("\n" + "=" * 60)
print("CONCEPT 5: normal - Custom Normal Distribution")
print("=" * 60)

# Example
print("\nExample 1: 5 numbers with mean=10, std=2")
print(np.random.normal(10, 2, 5))

print("\nExample 2: 2x3 matrix with mean=-5, std=3")
print(np.random.normal(-5, 3, (2, 3)))


print("\n" + "-" * 40)
print("YOUR ANSWERS:")
print("Task 1: 8 numbers with mean=20, std=5")
print(np.random.normal(20, 5, 8))

print("\nTask 2: 3x3 matrix with mean=-2, std=1.5")
print(np.random.normal(-2, 1.5, (3, 3)))

# ============================================================
print("\n" + "=" * 60)
print("CONCEPT 6: seed - Reproducible Results")
print("=" * 60)


print("\n" + "-" * 40)
print("YOUR ANSWERS:")
print("Task 1: Set seed 42 and generate 5 random numbers with rand()")
np.random.seed(42)
print(np.random.rand(5))

print("\nTask 2: Set seed 100 and generate 2x3 integers between 1 and 50")
np.random.seed(100)
print(np.random.randint(1, 50, (2, 3)))

# ============================================================
print("\n" + "=" * 60)
print("CONCEPT 7: choice - Random Sample from Array")
print("=" * 60)

arr = np.array([5, 10, 15, 20, 25, 30, 35, 40])
print(f"\nBase array: {arr}")


print("\n" + "-" * 40)
print("YOUR ANSWERS:")
print("Task 1: Randomly select 4 elements (with replacement)")
print(np.random.choice(arr, 4))

print("\nTask 2: Randomly select 4 elements (NO replacement)")
print(np.random.choice(arr, 4, replace=False))

# ============================================================
