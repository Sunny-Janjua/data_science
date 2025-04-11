# NumPy Detailed README Guide 📘🧮

Welcome to the **NumPy README**! This document provides a detailed guide on the most important and commonly used functions of the NumPy library. NumPy is a powerful Python library for numerical computing. It supports multi-dimensional arrays, mathematical operations, and statistical analysis efficiently.

---

## 📦 Installation

```bash
pip install numpy
```

---

## 🔢 Creating Arrays

```python
import numpy as np
```

### 1. `np.array()`
Creates a NumPy array from a Python list or tuple.
```python
arr = np.array([1, 2, 3])
```

### 2. `np.zeros()`
Creates an array filled with zeros.
```python
zeros = np.zeros((2, 3))
```

### 3. `np.ones()`
Creates an array filled with ones.
```python
ones = np.ones((2, 3))
```

### 4. `np.full()`
Creates an array filled with a specific value.
```python
filled = np.full((2, 2), 7)
```

### 5. `np.eye()`
Creates an identity matrix.
```python
identity = np.eye(3)
```

### 6. `np.arange()`
Creates an array with a range of values.
```python
range_array = np.arange(0, 10, 2)
```

### 7. `np.linspace()`
Creates an array with evenly spaced values.
```python
linspace_array = np.linspace(0, 1, 5)
```

### 8. `np.random.rand()`
Creates an array of given shape with random samples from a uniform distribution over `[0, 1)`.
```python
random_uniform = np.random.rand(2, 3)
```

### 9. `np.random.randn()`
Random samples from the standard normal distribution.
```python
random_normal = np.random.randn(2, 3)
```

---

## 🎲 Random Methods

### 1. `np.random.seed()`
Sets the seed for reproducibility.
```python
np.random.seed(42)
```

### 2. `np.random.randint()`
Returns random integers from a specified range.
```python
rand_ints = np.random.randint(0, 10, size=(2, 3))
```

### 3. `np.random.choice()`
Generates a random sample from a given 1D array.
```python
sample = np.random.choice([10, 20, 30], size=2)
```

### 4. `np.random.shuffle()`
Shuffles the contents of the array in place.
```python
arr = np.array([1, 2, 3, 4])
np.random.shuffle(arr)
```

### 5. `np.random.permutation()`
Returns a shuffled version of the input without modifying the original.
```python
arr = np.array([1, 2, 3, 4])
shuffled = np.random.permutation(arr)
```

---

## ⚙️ Array Operations

### 1. Arithmetic Operations
```python
arr + 1
arr * 2
arr - arr2
arr1 / arr2
```

### 2. Aggregation Functions
```python
np.sum(arr)
np.mean(arr)
np.std(arr)
np.var(arr)
np.min(arr)
np.max(arr)
np.argmin(arr)
np.argmax(arr)
```

### 3. Array Manipulation
```python
arr.reshape((3, 2))
arr.flatten()
arr.transpose()
np.concatenate((arr1, arr2))
np.vstack((arr1, arr2))
np.hstack((arr1, arr2))
```

### 4. Indexing & Slicing
```python
arr[0]
arr[1:4]
arr[:, 0]  # All rows, first column
arr[0, :]  # First row, all columns
```

---

## 🧠 Logical Operations

### 1. Conditions
```python
arr > 5
np.where(arr > 5, 1, 0)
np.any(arr > 5)
np.all(arr > 0)
```

### 2. Boolean Indexing
```python
arr[arr > 3]
```

---

## 🔄 Copy vs View

```python
copy = arr.copy()  # Creates a true copy
view = arr.view()  # Creates a view (shallow copy)
```

---

## 🧱 Matrix Operations

```python
np.dot(arr1, arr2)
np.matmul(arr1, arr2)
np.linalg.inv(matrix)
np.linalg.det(matrix)
np.linalg.eig(matrix)
```

---

## 🧾 Summary
NumPy is an essential library for data science and scientific computing. Understanding these core functions will help you harness its full power.

---

Happy Coding! 💻🚀

