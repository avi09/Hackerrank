def gets(s):
    subs = [s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]


    return subs
'''Now we will write a recursive function'''
'''Solution to hackerrank algorithms hard question 6'''
ans=[]
def f(x1,x2,a,b,n1,n2):
    global ans
    if len(x1) == n2:
        ans.append(n1)
        return
    for i in range(1):
        x=i
    if len(x2)==1:
        f(x1+x2[x],'',a,b,n1+a,n2)
    else:
        f(x1+x2[x],x2[1:],a,b,n1+a,n2)
    tm=gets(x1)
    tm2=[]
    for i in tm:
        if x2.find(i) == x:
            tm2.append([i,len(i)])
    tm2=sorted(tm2,key=lambda x:x[1])
    if tm2!=[]:
        f(x1+tm2[-1][x],x2[tm2[-1][1]:],a,b,n1+b,n2)


    return

x2='aabaacaba'
x1=''
a=4
b=5
for i in range(1):
    x=i
x1+=x2[x]
x2=x2[1:]
n1=a
n2=9
f(x1,x2,a,b,n1,n2)
print(min(ans))