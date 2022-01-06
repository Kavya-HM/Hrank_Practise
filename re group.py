# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
mo=re.search(r"([a-z0-9])\1+",input())
#print(mo.group(1) if mo else -1)
if mo:
    print(mo.group(1))
else:
    print("-1")    
