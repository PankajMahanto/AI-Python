
# Binary Search Algorithm apply using python

def BS(arr,s,l,r):
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]==s:
            return mid
        elif arr[mid]>s:
            r=mid-1
        else:
            l=mid+1
    return -1
        
def Bsort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                
            
     
def printArr(arr):
    for i in range(len(arr)):
        print (arr[i],end=' ')

        
        
arr =[]
n=int(input("Enter how many numbers do you input: "))

# for i in range(n):
arr=list(map(int,input("element: ").strip().split()))[:n]

print("\nArray before sort: ")
printArr(arr)
Bsort(arr)
print("\nArray after sort: ")
printArr(arr)
#Which Value you Search?
search=int(input("\nEnter the Search value: "))
l=0
r=n-1
value=BS(arr,search,l,r)

if value==-1:
    print("\nvalue: ",search," Not find in the Array")
else:
    print("\nvalue: ",search,"Find in the Array",value)