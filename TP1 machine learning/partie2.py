import numpy as np
revenus = [1800, 1500, 2200, 3000, 2172]

def moyenne(liste):
    total = 0
    for elem in liste:
        total=total+elem
    return total/len(liste)



revenus2 = np.array([1800, 1500, 2200, 3000, 2172])
np.mean(revenus2)
np.argmax(revenus2)
np.argmin(revenus2)   

revenus2.sort()

print(revenus2[1] ,revenus2[2] ,revenus2[3])

def elemSurDeux(liste):
    list = []
    i=0
    while(i<len(liste)):
        list.append(liste[i])
        i=i+2
    return list

 
print(elemSurDeux(revenus2));  

 
arr = np.array([[5,3,8],[9,6,5],[7,5,9],[3,2,4]])
arr1 = np.vstack([arr,[5,2,4]])

arr2 = np.delete(arr,3,0)
print(arr2)



def supp2000(liste):
    list = []
    i=0
    while i<len(liste):
        if liste[i]>2000:
            list.append(liste[i])
            i=i+1
    return list

print(supp2000(revenus2))   