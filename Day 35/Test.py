import numpy as np

sampleArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(sampleArray)

arr = sampleArray[1,:]
sampleArray = np.delete(sampleArray , 1, axis = 1)
sampleArray = np.insert(sampleArray , 1, arr, axis = 1)
print(sampleArray)


sampleArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr = sampleArray[1,:]
sampleArray[:,1]=arr
print(sampleArray)



#sampleArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
#arr = sampleArray[1,:]
#sampleArray = np.delete(sampleArray , 1, axis = 1)
#sampleArray = np.insert(sampleArray , 1, arr, axis = 0)
#print(sampleArray)


#sampleArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
#arr = sampleArray[0,:]
#sampleArray = np.delete(sampleArray , 1, axis = 1)
#sampleArray = np.insert(sampleArray , 1, arr, axis = 0)
#print(sampleArray)
