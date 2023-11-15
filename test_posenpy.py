import numpy as np

npypath = '/home/wtxt/share-backup/132chip_test/poses_bounds.npy'
arr = np.load(npypath)
arr = arr[:13]
np.save(npypath,arr, )
print(arr.shape)
