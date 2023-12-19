print("Rail_fence algorithms:")
string=input("Enter the string:")
t=[]
def encry(string):
  tt=len(string)
  if (tt%2) == 0:
    for i in string:
      if (string.index(i)%2) == 0:
        t.append(i)
        
    for i in string:
      if (string.index(i)%2)!= 0:
        t.append(i)
  else:
    for i in string:
      if (string.index(i)%2) == 0:
        t.append(i)      
    for i in string:
      if (string.index(i)%2)!= 0:
        t.append(i)       
encry(string)
print(t)
