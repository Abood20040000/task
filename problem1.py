#task1

arr=[]
import math

def add_num(length):
    for i in range(length):
        x=int(input("Enter:"))
        arr.append(x)   

length=int(input("Enter the length:"))
add_num(length)
arr.sort()

hours=int(input("Enter the num of hours:"))        

def koko(arr,hours):
    

    theMax=arr[length-1]
    theMin=1

    k=0
    while(theMin<theMax):
        mid=(theMax+theMin)//2
        k=0
        for i in range(length):
            k+=math.ceil(arr[i]/mid)
    
        if (k>hours):
            theMin=mid+1
        else:
            theMax=mid

    return theMin

k=koko(arr,hours)
print(k)
            



        




