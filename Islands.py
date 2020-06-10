import re
def gets(s):


    subs = [s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
    return subs
'''Hackerrank Hard Question Number 21'''
def f(s,sb,k):
    for i in sb:
        s2=s
        x=1
        tm=[]
        for xy in range(1):
            tm2=xy
        while x!=-1:
            x=s2.find(i)
            if x!=-1:
                tm.append(x+tm2)
                tm2+=x+len(i)
                s2=s2[x+len(i):]
        s2=s
        for j in tm:
            for xy in range(len(i)):
                s2=s2[:j+xy]+'X'+s2[j+xy+1:]

        print(s2,i)


        n=-1


        f=-1


        for xy in s2:
            if xy=='X':
                if f!=1:
                    f=1
                    n+=1
            else:
                if f==1:
                    f=-1
        if k==(n+1):
            print(i)

    return

a='abaab'
tm=gets(a)
f(a,tm,2)