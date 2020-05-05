import country_tools as ct
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sb

# this is just downloading a random data set I downloaded, has to be replaced by our data
# from sklearn.datasets import load_breast_cancer
# data = load_breast_cancer()

names = ["Fuelburn", "NO2", "HC", "CO", "BC", "PM25", "AerMassSO4", "AerMassNIT", "AerMassNH4", "AerMassPOA",
         "AerMassBC", "O3"]

data = ct.find_matrix_data(ct.POLLUTION_COLLECTIONS, slice(0,32), True)
df = pd.DataFrame.from_dict(data, orient='index', columns=names)

# change to dataFrame
# df = pd.DataFrame(data.data, columns=data.feature_names)

corr_type = 'pearson' # for a different correlation indicator, try method='spearman' or method='kendall'
corr_df = corr = df.corr(method=corr_type) #calculate correlation matrix
df_lt = corr_df.where(np.tril(np.ones(corr_df.shape)).astype(np.bool))

hmap=sb.heatmap(df_lt,cmap="coolwarm", vmin=-0.9, vmax=1)

plt.show()