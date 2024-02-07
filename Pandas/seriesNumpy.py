import numpy as np
import pandas as pd
data_ls=[10,20,30,40,50]
ndata = np.array(data_ls)
ps=pd.Series(ndata)
print(ps)