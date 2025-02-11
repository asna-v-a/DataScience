import numpy as np
import urllib.request

# URL of the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Specify the folder location where you want to save the file
save_path = "C:/Users/asnav/Desktop/DataScience/PythonDS/10_numpy_basics/url_iris.data"  # Update as needed

# Download and save the file
urllib.request.urlretrieve(url, save_path)

print(f"File downloaded and saved at: {save_path}")

# Load the dataset from the saved file
data = np.genfromtxt(save_path, delimiter=",", dtype=str)

# Check if data loaded correctly
if data.ndim == 1:
    print("Error: Data not loaded correctly. Check file format.")
else:
    print("Data loaded successfully!")

# Remove rows with missing values
data = data[~np.any(data == '', axis=1)]

# Extract the petal lengths (3rd column) as floats
petal_lengths = data[:, 2].astype(float)

# Categorize the petal lengths
categories = np.where(petal_lengths < 3, 'small',
                      np.where(petal_lengths < 5, 'medium', 'large'))
print("Petal length categories:", categories)

# Filter rows where the species is 'Iris-setosa' and get petal lengths
species_column = data[:, -1]  # Last column contains species
setosa_mask = species_column == "Iris-setosa"

if np.any(setosa_mask):
    setosa_petal_lengths = petal_lengths[setosa_mask]
    
    # Sort and get the second longest petal length
    sorted_lengths = np.unique(np.sort(setosa_petal_lengths))
    
    if len(sorted_lengths) > 1:
        print("Second longest petal length of Iris-setosa:", sorted_lengths[-2])
    else:
        print("Not enough unique values for second longest petal length.")
else:
    print("No 'Iris-setosa' species found in data.")
