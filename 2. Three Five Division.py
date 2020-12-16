ans=[]
for i in list(range(0,1001)):
    if i % 5 == 0 or i % 3 == 0:
     ans.append(i)
s=sum(ans)
print(s)
