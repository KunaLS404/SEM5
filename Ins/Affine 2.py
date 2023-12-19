dataset=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
arr=[]
arr2=[]
arr3=[]
arr4=[]
arr5=[]


def encryption(text,key,key2):
    print(end="\n")
    print("Text with his unique number")
    for i in text:
        arr.append(i)
        print(i,end=" ")
        temp1=dataset.index(i)
        print(temp1,end=" ")
        print(end="\n")
    
      
    for i in arr:
        temp=dataset.index(i)*key
        arr2.append(temp)
    for i in arr2:
        i=i%len(dataset)
        arr3.append(dataset[i])
    print("Multiplicative cipher for plain text")
    for i in arr3:
        print(i,end=" ")
        print(dataset.index(i),end=" ")
        print(end="\n")
        
    for i in arr3:
        temp=dataset.index(i)+key2
        arr4.append(temp)
    for i in arr4:
        i=i%len(dataset)
        arr5.append(dataset[i])
    
    print("Text after encryption method")
    for i in arr5:
        print(i,end=" ")
        print(dataset.index(i),end=" ")
        print(end="\n")
        
    arr.clear()
    exit()

def decryption(text,key,key2):
    print(end="\n")
    print("Text with his unique number")
    for i in text:
        arr.append(i)
        
        temp1=dataset.index(i)
        print(i," ",temp1,end=" ")
        print(end="\n")
    for i in arr:
        temp=dataset.index(i)-key2
        arr2.append(dataset[temp])
    print("Text with sustititive cipher with its unique number")
    for i in arr2:
        temp=dataset.index(i)
        print(i," ",temp,end=" ")
        print(end="\n")
        arr3.append(dataset[temp])
    print("Decryption text after multiplicative inverse with its unique number")
  
    for i in arr3:
       temp=dataset.index(i)
       for j in range(0,25):
           if (key*j)%26==temp:
               print(dataset[j],"  ",j)
        
    exit()


    
a=int(input("Enter 0 for Encryption or 1 for Decryption"))
if a==0:
    x=input("Enter Text: ")
    y=int(input("Enter Key: "))
    z=int(input("Enter key2:"))
    print("*****************************************************************")
    print("Enter text is ",x,".")
    encryption(x,y,z)
    
elif a==1:
    x=input("Enter decrypted text: ")
    y=int(input("Enter Key: "))
    z=int(input("Enter key2:"))
    decryption(x,y,z)
    

    
    







        
