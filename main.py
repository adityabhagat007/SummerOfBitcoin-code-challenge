import pandas as pd
import numpy as np

df = pd.read_csv("mempool.csv")

# sorting in descending order of fee
sdf = df.sort_values(by=["fee"], ascending=False)

dataframe = pd.DataFrame(sdf['tx_id'])
# print(dataframe)

np_array = dataframe.to_numpy()
# print(numpy_array)

# displaying the tx_id in block.txt file

length = len(np_array)
file = open("block.txt","a")
for i in range(length):
    file.write(str(np_array[i][0])+'\n')
file.close()
print("Output is in block.txt file ")