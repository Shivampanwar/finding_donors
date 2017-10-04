import numpy as np
import pandas as pd
from time import time
from IPython.display import display # Allows the use of display() for DataFrames
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier

# Build a classification task using 3 informative features
d = {'one' : pd.Series([1., 2., 3.,66.], index=['a', 'b', 'c','d']), 'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),'three' : pd.Series([11., 22., 33., 44.], index=['a', 'b', 'c', 'd'])}
fd=pd.DataFrame(d)


df=fd[fd.columns.values[:2]]
print df
print fd.columns.values