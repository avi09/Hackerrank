import re
'''Answer to Hackerrank algorithms Q2 hard. Finding the score for DNA sequence'''


def findDNA(x,a,b,sq,sqv,n):
    ans=[-1]*n
    
    for i in range(n):
        sq1 = sq[a[i]:b[i]+1]
        sqv1 = sqv[a[i]:b[i]+1]
        '''finding if a genome is there in the DNA'''

        for j in set(sq1):
            try:
                '''try to search for instance j in x'''
                tm=len([x1.start() for x1 in re.finditer(j,x[i])])
                y = [x1 for x1,x2 in enumerate(sq1) if x2==j]
                y1=-1
                for x1 in y:
                    y1+=sqv1[x1]
                y1+=1
                ans[i]+=tm*y1
            except Exception:
                print("Cannot find "+j+" in "+x)
        ans[i]+=1
    return ans

n=2
x=['bb','aa']
a=[1,1]
b=[5,5]


sq = ['a','b','c','aa','d','bbb']
sqv = [1,2,4,4,5,6]
print(findDNA(x,a,b,sq,sqv,n))


