def ia(x):
    
    
    if x==x[::-1]:
        return True
    else:
        return False

'''Hackerrank Hard Q 18 for borders'''
def find(s):
    tm=[]
    for i in range(len(s)):
        if s[:i+1]==s[len(s)-1-i:] and i!=len(s)-1:
            if ia(s[:i+1]):
                tm.append(s[:i+1])
    return tm
def circular(x):
    subs = [x[i:j] for i in range(len(x)) for j in range(i+1,len(x)+1)]
    ans=-1
    for i in subs:
        ans+=len(find(i))
    return ans+1
x='ababa'
print(circular(x))
