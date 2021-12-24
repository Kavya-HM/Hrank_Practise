text=int(input())
for i in range(text):
    string=input()
    if(len(string)==10 and (string[0]=='7' or string[0]=='8' or string[0]=='9') and string.isnumeric()):
        print("YES")
    else:
        print("NO")    
