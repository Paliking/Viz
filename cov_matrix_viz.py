
from matplotlib import pyplot as plt
from matplotlib import cm as cm
import pandas as pd
import numpy as np

def correlation_matrix(df):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap('jet', 60)
    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    ax1.grid(True)
    plt.title('Corelation Matrix visualization')
    labels=df.columns
    ax1.set_xticklabels(labels,fontsize=4)
    ax1.set_yticklabels(labels,fontsize=4)
    fig.colorbar(cax, ticks=[-0.6,-0.3,0,0.3,0.6])
    plt.show()


df = pd.DataFrame(data=np.random.rand(20,50))
correlation_matrix(df)



# ina cor. matrix
https://www.kaggle.com/yitzhakr/moscow-houses-prices-analysis
