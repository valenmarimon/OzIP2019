

import pandas as pd

original = pd.read_csv('fer2013-OZagus.csv',header=0)

#print(len(original))

original = original.drop_duplicates(subset='pixels', keep='first',inplace=False)

#print(len(original))

original.to_csv(r'fer2013-OZ-v2.0.csv',index=False)




