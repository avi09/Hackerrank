import re
def gets(s):


    subs = [s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
    return subs

def f(s,sb):
    x=-2
    n=-1
    while x!=-1:
        x=s.find(sb)
        if x!=-1:
            n+=1
        s=s[1:]
    return n+1

a='aaaaaa'
tm=gets(a)
x=[]
for i in tm:
    x.append(f(a,i)*len(i))
print(x,max(x))