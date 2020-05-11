import numpy as np

a=int(input("matrix sorainak szama: "))
b=int(input("matrix oszlopainak szama: "))
m=np.random.randint(0,9,(a,b))
def matrix_sorted_or_not(m):
    db = 0
    for i in range(m.shape[0]):
            k=str(m[i])
            k=k[1:-1]
            x=str(np.sort(m[i]))
            x=x[1:-1]
            rev=str(x[::-1])
            rev=rev[1:-1]
            if ((k==x) or (k==rev)) or (x==rev):
                db+=1
    if a>=b:
        for j in range(m.shape[1]):
            h = str(m[j])
            h=h[1:-1]
            y = str(np.sort(m[j]))
            y=y[1:-1]
            rev2 = str(y[::-1])
            rev2=rev2[1:-1]
            if ((h == y) or (h == rev2)) or (y==rev2):
                db += 1
    else:
        for j in range(0,m.shape[1]-(b-a)):
            h=str(m[j])
            h=h[1:-1]
            y=str(np.sort(m[j]))
            y=y[1:-1]
            rev2=str(y[::-1])
            rev2=rev2[1:-1]
            if ((h==y) or (h==rev2)) or (y==rev2):
                db+=1

        db+=(b-a)
    if a==2 and b==2:
        return True
    else:
        if db>=(a+b):
            return True
        else:
            return False

print(m)
print(matrix_sorted_or_not(m))

