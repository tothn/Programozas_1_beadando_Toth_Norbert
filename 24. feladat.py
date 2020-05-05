import numpy as np
def height_sort(x):
    j=np.sort(x[x!=-1])
    lst=[]
    for i in range(len(x)):
        if x[i]==-1:
            lst.append(i)
    for i in range(len(lst)):
        j=np.insert(j,lst[i],-1)
    return j

x = np.array([-1, 150, 190, 170, -1, -1, 160, 180])
print("Bemenet: {}".format(x))
print("Kimenet: {}".format(height_sort(x)))
