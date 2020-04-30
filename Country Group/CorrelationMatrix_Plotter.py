import country_tools as ct
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sb

# this is just downloading a random data set I downloaded, has to be replaced by our data
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()

# change to dataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)

corr_type = 'pearson' # for a different correlation indicator, try method='spearman' or method='kendall'
corr_df = corr = df.corr(method=corr_type) #calculate correlation matrix
df_lt = corr_df.where(np.tril(np.ones(corr_df.shape)).astype(np.bool))

hmap=sb.heatmap(df_lt,cmap="coolwarm")

plt.show()