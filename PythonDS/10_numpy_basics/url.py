"""
1.Write a NumPy program to test whether none of the elements of a given array are zero.
2. Write a NumPy program to create an array of integers from 30 to 70.
3.Write a NumPy program to create an array of all even integers from 30 to 70.
4. Get the common items between a and b
Input:
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
5. Reverse the columns of a 2D array arr.
# Input
arr = np.arange(9).reshape(3,3)

Note: Use this dataset for qn 6,7,8 : https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

6.Replace all occurrences of nan with 0  in numpy array
7. How to convert a numeric to a categorical (text) array?
Q. the petal length (3rd) column of iris_2d to form a text array, such that if petal length is:
Less than 3 --> 'small'
3-5 --> 'medium'
'>=5 --> 'large’

8. What is the value of second longest petal length of species setosa
9. Flatten a 2d numpy array into 1d array
10.Find the sum of values in a matrix

"""
import numpy as np

# Load the data from the local file
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = np.genfromtxt(url, delimiter=",", dtype=str)

# Extract the petal lengths (3rd column) as floats
petal_lengths = data[:, 2].astype(float)

# Categorize the petal lengths
categories = np.where(petal_lengths < 3, 'small', np.where(petal_lengths < 5, 'medium', 'large'))
print("Petal length categories:", categories)

# Filter rows where the species is 'Iris-setosa' and get petal lengths
species = petal_lengths[data[:, 4] == 'Iris-setosa']
print("Petal lengths of Iris-setosa:", species)

s=np.unique(np.sort(species))
print(s[-2])
