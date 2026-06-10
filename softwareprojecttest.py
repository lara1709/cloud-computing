import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


data = pd.read_excel(r"c:\Users\larag\Downloads\Class3_Practical.xlsx")


data = data.drop_duplicates()

data.head()