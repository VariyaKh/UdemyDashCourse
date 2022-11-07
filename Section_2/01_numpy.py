import numpy as np

my_list = [1, 2, 3, 4, 5]

array = np.array(my_list)

print(np.arange(0, 10))
print(np.arange(0, 10, 2))
print(np.zeros((5, 5)))
print(np.zeros((2, 10)))
print(np.ones((2, 4)))

print(np.random.randint(0, 100))
print(np.random.randint(0, 100))
print(np.random.randint(0, 100))
print(np.random.randint(0, 100, (5, 5)))

print(np.linspace(0, 10, 6))
print(np.linspace(0, 10, 101))

np.random.seed(42)
print(np.random.randint(0, 100))
print(np.random.randint(0, 100))
print(np.random.randint(0, 100))

array = np.random.randint(0, 100, 10)
print(array)
print('max', np.max(array))
print('min', np.min(array))
print('mean', np.mean(array))
print('argmax', np.argmax(array))
print('argmin', np.argmin(array))

print('rashape', array.reshape(2, 5))

mat = np.arange(0, 100).reshape(10, 10)
print(mat)
print(mat[5, 2])
print(mat[:, 2])
print(mat[2, :])
print(mat[mat > 50])