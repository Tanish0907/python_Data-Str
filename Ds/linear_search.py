def l_search(arr:list,key):

    for i in range(len(arr)):
        if arr[i] == key:
            return i
        else:
            return -1
def main():
    l=[]
    n=int(input("Enter the number of elements: "))
    for i in range(n):
        l.append(int(input("Enter the element: ")))

    key=int(input("Enter the key: "))
    i=l_search(l,key)
    if i==-1:
        print(f"{key} not found")
    else:
        print(f"{key} is found at index {i}")   
if __name__ == "__main__":
    main()