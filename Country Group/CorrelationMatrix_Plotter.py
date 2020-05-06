import country_tools as ct
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sb

summer = False
emission_levels = slice(0, 32)
with_scatterplots = False

names = ["Fuelburn", "NO2", "HC", "CO", "BC", "PM25", "AerMassSO4", "AerMassNIT", "AerMassNH4", "AerMassPOA",
         "AerMassBC", "O3"]

data = ct.find_matrix_data(ct.POLLUTION_COLLECTIONS, emission_levels, summer)
df = pd.DataFrame.from_dict(data, orient='index', columns=names)

corr_type = 'pearson'  # for a different correlation indicator, try method='spearman' or method='kendall'
corr_df = corr = df.corr(method=corr_type)  # calculate correlation matrix
df_lt = corr_df.where(np.tril(np.ones(corr_df.shape)).astype(np.bool))

hmap = sb.heatmap(df_lt, cmap="coolwarm", vmin=-0.9, vmax=1, annot=True, cbar=False)

plt.title("Emission levels: " + str(emission_levels.start) + " to " + str(emission_levels.stop) +
          " | " + ("July" if summer else "January") + " 2005")

if with_scatterplots:
    plt.savefig("MatrixOutput/Correlation matrix")

    for i in range(int(np.ceil(len(names) / 2))):
        for j in range(len(names)):
            if i != j:
                plt.figure()
                plt.title("Emission levels: " + str(emission_levels.start) + " to " + str(emission_levels.stop) +
                      " | " + ("July" if summer else "January") + " 2005")
                x = df[names[i]]
                y = df[names[j]]
                plt.scatter(x, y)
                plt.axis([min(x), max(x), min(y), max(y)])
                plt.xlabel(names[i])
                plt.ylabel(names[j])
                plt.savefig("MatrixOutput/Scatter plot " + names[i] + " vs " + names[j])

else:
    plt.show()
