def merge(arr:list,fi,li):
    if fi==li:
        return arr
    else:
        mid=(fi+li)//2
        merge(arr,fi,mid)
        merge(arr,mid+1,li)
        mp(arr,fi,mid,li)
        return arr
def mp(arr:list,fi,mid,li):
    b=[]
    i=fi
    k=mid+1
    while(i<=mid and k<=li):
        if(arr[i]<arr[k]):
            b.append(arr[i])
            i+=1
        else:
            b.append(arr[k])
            k+=1
    while(i<=mid):
        b.append(arr[i])
        i+=1 
           
    while(k<=li):
        b.append(arr[k])
        k+=1 
    for i in range(len(b)):
        arr[fi+i]=b[i]
def main():
    l=[]
    n=int(input("Enter the number of elements: "))
    for i in range(n):
        l.append(int(input("Enter the element: ")))
    l=merge(l,0,n-1)
    print(l)
if __name__ == "__main__":
    main()