arr=[]

length=int(input("Enter the length: "))
def add_num(length):
    for i in range(length):
        x=int(input("Enter:"))
        arr.append(x)

add_num(length)


def rob():
    if len(arr)<=2:
        return max(arr)
    
    robbed=arr[0]
    robbing=max(arr[0],arr[1])

    for i in range(2,len(arr)):
        temp=robbing
        robbing=max(robbed+arr[i],robbing)
        robbed=temp

    return robbing

print(rob())
    
   

       