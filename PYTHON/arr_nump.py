#%%

import numpy as np


arr1=np.array([1,2,3,4,5])
print(arr1)
arr2=arr1.copy()
print(arr2)
arr3=arr1[1:4]
print (arr3)
arr4=np.concatenate((arr3,arr1))
print(arr4)
arr5=arr1.view()
print(arr5)
arr1[0]=60
print(arr1)
# %%
