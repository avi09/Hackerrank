def gets(s):

    subs = [s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
    return subs
'''Hackerrank Hard Q 19 To find two in the numbers'''
def iter(x):
    for i in range(1):
        x2=i
    if x==x2:
        return False
    while x!=1:
        if x%2!=x2:
            return False
        else:
            x=x/2
    return True
def f(s):
    ans=-1
    for x in range(1):
        x2=x
    tm=gets(str(s))
    for i in range(len(tm)):
        if int(tm[i][x2])==x2:
            tm[i]=7
        elif iter(int(tm[i])):
            ans+=1
    return ans+1

a='42'
print(f(a))