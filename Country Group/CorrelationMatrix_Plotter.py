import country_tools as ct
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sb

summer = False
emission_levels = slice(0, 32)
save_with_scatterplots = True
with_labels = True

names = ["Fuelburn", "NO$_{x}$", "HC", "CO", "BC ", "O$_{3}$", "PM$_{2.5}$", "SO$_{4}$", "NIT", "NH$_{4}$", "POA",
         "BC"]


data = ct.find_matrix_data(ct.POLLUTION_COLLECTIONS, emission_levels, summer)
df = pd.DataFrame.from_dict(data, orient='index', columns=names)

corr_type = 'pearson'  # for a different correlation indicator, try method='spearman' or method='kendall'
corr_df = df.corr(method=corr_type)  # calculate correlation matrix
df_lt = corr_df.where(np.tril(np.ones(corr_df.shape)).astype(np.bool))

df_lt = df_lt.drop(names[:5])
df_lt = df_lt.drop(names[5:], axis=1)

plt.rcParams.update({'font.size': 12})
hmap = sb.heatmap(df_lt, cmap="coolwarm", annot=True, cbar=True, vmin=-1, vmax=1)
plt.xlabel("Emission species")
plt.ylabel("Pollutant species")

plt.title("Emission levels: " + str(emission_levels.start) + " to " + str(emission_levels.stop) +
          " | " + ("July" if summer else "January") + " 2005")

if save_with_scatterplots:
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
                if with_labels:
                    for ci in range(len(x)):
                        plt.annotate(df.index.values[ci], [x[ci], y[ci]])
                plt.savefig("MatrixOutput/Scatter plot " + (names[i] + " vs " + names[j]).replace(".", ""))

    print("All figures saved to current directory")

else:
    plt.show()
