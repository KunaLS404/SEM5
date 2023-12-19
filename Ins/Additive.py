dataset=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

arr=[]
arr2=[]
arr3=[]


def encryption(text,key):
    print(end="\n")
    print("Text with his unique number")
    for i in text:
        arr.append(i)
        print(i,end=" ")
        temp1=dataset.index(i)
        print(temp1,end=" ")
        print(end="\n")
    
      
    for i in arr:
        temp=dataset.index(i)+key
        arr2.append(temp)
    for i in arr2:
        i=i%len(dataset)
        arr3.append(dataset[i])
    
    print("Text after encryption method")
    for i in arr3:
        print(i,end=" ")
        print(dataset.index(i),end=" ")
        print(end="\n")
        
    arr.clear()
    exit



def decryption(text,key):
    print("Text for decryption method with its unique number:")
    if key>25:
        key=key%len(dataset)

    for i in text:
        arr2.append(i)
        print(i,end=" ")
        temp1=dataset.index(i)
        print(temp1,end=" ")
        print(end="\n")
    print(end="\n")
    
    
    for i in arr2:
        temp=dataset.index(i)-key
        arr.append(dataset[temp])

    print("Text after decryption method with unique number:")
    for i in arr:
        print(i,end=" ")
        print(dataset.index(i),end=" ")
        print(end="\n")
        
    
        
        
    exit()


    
a=int(input("Enter 0 for Encryption or 1 for Decryption"))
if a==0:
    x=input("Enter Text: ")
    y=int(input("Enter Key: "))
    encryption(x,y)
elif a==1:
    x=input("Enter decrypted text: ")
    y=int(input("Enter Key: "))
    decryption(x,y)
    

    
    







        
