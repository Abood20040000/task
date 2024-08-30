arr2 = [[1,3],[2,6],[8,10],[15,18]]
arr=[[1,4],[4,5]]
newArr=[]

for i in range(1,len(arr)):
    if(arr[i][0]<=arr[i-1][1]):
        newArr.append([arr[i-1][0],arr[i][1]])
    else:
        newArr.append(arr[i])

           

print(newArr)        




        
