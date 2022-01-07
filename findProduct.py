n=int(input())
array=map(int,input().split())
ans=1
for i in array:
    ans=(ans*i)%((10**9)+7)
print(ans)
