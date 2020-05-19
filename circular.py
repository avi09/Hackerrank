def ia(x):
    
    
    if x==x[::-1]:
        return True
    else:
        return False

'''Hackerrank Hard Q 14 circular answer'''
def circular(x):
    tm=[]
    for i in range(len(x)):
        tm.append(x[i:]+x[:i])
    tm2=[]
    for xy in tm:
        subs = [xy[i:j] for i in range(len(xy)) for j in range(i+1,len(xy)+1)]
        maxm=-1
        for yy in subs:
            if ia(yy) and len(yy)>maxm:
                maxm=len(yy)
        tm2.append(maxm)
    return tm2

x='abxy'
print(circular(x))
