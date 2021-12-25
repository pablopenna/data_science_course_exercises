import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns 

PATH='./dog vs cat/dataset/'
PATH_TRAIN='training_set/'
PATH_TEST='test_set/'

ids_cats = [f'cat.{i}' for i in range(1, 5_001)]
ids_dogs = [f'dog.{i}' for i in range(1, 5_001)]

df_all = pd.DataFrame({
    'id': ids_cats + ids_dogs,
    'target': [0 for _ in range(5_000)] + [1 for _ in range(5_000)],
    'target_label': ['cats' for _ in range(5_000)] + ['dogs' for _ in range(5_000)],
    'subset': ['train' for _ in range(4_000)] + ['train' for _ in range(4_000)] + ['test' for _ in range(1_000)] + ['test' for _ in range(1_000)]
})