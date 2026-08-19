import numpy as np

arr1 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9],
                 [10,11,12]])
# Accessing column.

print(f"\n{arr1[0:2, 1:]}")
print(f"\n{arr1[-2:]}")
print(f"\n{arr1[:, 0:2]}")
print(f"\n{np.transpose(arr1[1:, 1:2])}")
print(f"\n{arr1[2:,1:]}")
print(f"\n{arr1[0:3:2, 0::2]}")
print(f"\n{arr1[1]}")
print(f"\n{arr1[0:3:2,1:2:1]}")
print(f"\n{np.flipud(arr1)}")  #Flip upside down
print(f"\n{np.fliplr(arr1)}")  #Flip left to right



