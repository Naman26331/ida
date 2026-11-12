import numpy as np
# Creating arrays
a = np.array([10, 20, 30, 40, 50, 60])
b = np.arange(1, 13).reshape(3, 4)
print("1-D array a:", a)
print("2-D array b:\n", b)
print("zeros(2, 3):\n", np.zeros((2, 3)))
print("ones(2, 2) :\n", np.ones((2, 2)))
print("linspace   :", np.linspace(0, 1, 5))

# Indexing
print("\na[0] =", a[0], ", a[-1] =", a[-1])
print("b[1, 2] =", b[1, 2])

# Slicing
print("\na[1:4]  :", a[1:4])
print("a[::2]  :", a[::2])
print("b[:2, 1:3]:\n", b[:2, 1:3])
print("b[:, 0] (first column):", b[:, 0])
print("b[2] (last row)       :", b[2])

# Boolean indexing
print("a[a > 30]:", a[a > 30])

# Reshaping
print("\nShape of b :", b.shape)
print("b.reshape(4, 3):\n", b.reshape(4, 3))
print("b.reshape(2, 6):\n", b.reshape(2, 6))
print("b.reshape(-1)  :", b.reshape(-1))
print("b.flatten()    :", b.flatten())
print("b.T (transpose):\n", b.T)
