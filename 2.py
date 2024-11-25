import numpy as np

matrix = np.load('./resources/second_task.npy')

x, y, z = [], [], []

for i in range(matrix.shape[0]):
  for j in range(matrix.shape[1]):
    if matrix[i, j] > 504:
     try:
      if matrix[i, j] > matrix[i, j+1]:
        x.append(i)
        y.append(j)
        z.append(matrix[i, j])
     except IndexError:
      if matrix[i, j] > matrix[i-1,j]:
       x.append(i)
       y.append(j)
       z.append(matrix[i,j])
      
x = np.array(x)
y = np.array(y)
z = np.array(z)

np.savez('./data.npz', x=x, y=y, z=z)
np.savez_compressed('./data_compressed.npz', x=x, y=y, z=z)

import os
size_uncompressed = os.path.getsize('./data.npz')
size_compressed = os.path.getsize('./data_compressed.npz')

print(f"Размер файла data.npz: {size_uncompressed} байт")
print(f"Размер файла data_compressed.npz: {size_compressed} байт")
print(f"Сжатие: {size_uncompressed - size_compressed} байт")