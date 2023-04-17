def bin(arr:list,key,fi,li):

    if fi==li:
        if arr[fi]==key:
            print(f"{key} is found at index {fi}")   
        else:
            print(f"{key} not found")
    else:
        mid=(li+fi)//2
        if arr[mid]==key:
            print(f"{key} is found at index {mid}")   
        elif arr[mid]>key:
            li=mid-1
            bin(arr,key,fi,li)
        else:
            fi=mid+1
            bin(arr,key,fi,li)
        
def main():
    l=[]
    n=int(input("Enter the number of elements: "))
    for i in range(n):
        l.append(int(input("Enter the element: ")))

    key=int(input("Enter the key: "))
    bin(l,key,0,n-1)
if __name__ == "__main__":
    main()