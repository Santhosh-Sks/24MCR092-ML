from pandas import  read_csv
from matplotlib import pyplot 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

#step 1 : load the dataset
filename  = "Iris.csv"
data = read_csv(filename)

#step 2 : split the dataset into features and target variable
print()
