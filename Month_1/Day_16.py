import numpy as np

# Equations:
# 3x + y = 9
# x + 2y = 8
A = np.array([[3, 1], 
              [1, 2]])

B = np.array([9, 8])

solution = np.linalg.solve(A, B)

print("Solution:")
print(f"X = {solution[0]}")
print(f"Y = {solution[1]}")
