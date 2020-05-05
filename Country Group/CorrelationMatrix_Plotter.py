import country_tools as ct
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sb

summer = True
emission_levels = slice(0, 32)

names = ["Fuelburn", "NO2", "HC", "CO", "BC", "PM25", "AerMassSO4", "AerMassNIT", "AerMassNH4", "AerMassPOA",
         "AerMassBC", "O3"]

data = ct.find_matrix_data(ct.POLLUTION_COLLECTIONS, emission_levels, summer)
df = pd.DataFrame.from_dict(data, orient='index', columns=names)

corr_type = 'pearson'  # for a different correlation indicator, try method='spearman' or method='kendall'
corr_df = corr = df.corr(method=corr_type)  # calculate correlation matrix
df_lt = corr_df.where(np.tril(np.ones(corr_df.shape)).astype(np.bool))

hmap = sb.heatmap(df_lt, cmap="coolwarm", vmin=-0.9, vmax=1, annot=True, cbar=False)

plt.title("Correlation Matrix\n\nEmission levels: " + str(emission_levels.start) + " to " + str(emission_levels.stop) +
          " | " + ("July" if summer else "January") + " 2005")

plt.show()
