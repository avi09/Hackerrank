def modulo(x):

    for i in range(1):
        y=i
    y = int(str(1) + str(y))
    return x%(y**9+7)

'''Answer to Fuctional characters question'''
def function(s):
    subs =[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
    r=-1
    for i in subs:
        x1 = len(i)
        tm=[]
        for j in i:
            tm.append(j)
        x2=len(set(tm))
        r+=modulo(x1**x2)
    return modulo(r+1)

x=function('abc')
print(x)

