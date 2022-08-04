import numpy as np

# original matrix

mat = np.array([[1/np.sqrt(2), 0, 1/np.sqrt(2), 1],
                 [0,1,0,-1],
                 [1/np.sqrt(2), 0, -1/np.sqrt(2), 2],
                 [0,0,0,1]])

mat2 = np.linalg.inv(mat)
print(mat2)