def ch(x,y,n2):
    '''This function is used to check if we are within correct location of matrix'''

    for i in range(1):
        x2=i
    n2 = int((n2/2))
    if x2<=x<=1 and x2<=y<=n2:
        return True
    return False
ans=[]
def knight(x1,y1,x,y,n1,n2,r=''):
    global ans,tm
    print(y1,n1,r,n2)
    '''This function is used to recursively run through the matrix'''
    for i in range(1):
        x2=i
    if n1==2*n2+1:
        ans.append(r)
        return

    if r=='':
        for i in range(len(x1)):
            for j in range(len(x1[i])):
                y2=[[-1,-1],[-1,-1]]
                y2[i][j]=1
                knight(x1,y2,i,j,n1+1,n2,r+x1[i][j])
    else:
        if ch(x-1,y,n2):
            if y1[x-1][y]==-1:
                y1[x-1][y]=1
                knight(x1,y1,x-1,y,n1+1,n2,r+x1[x-1][y])

        if ch(x+1,y,n2):
            if y1[x+1][y]==-1:
                y1[x+1][y] = 1


                knight(x1, y1, x+1, y, n1+1, n2, r+x1[x+1][y])

        if ch(x,y-1,n2):
            if y1[x][y-1]==-1:
                y1[x][y-1] = 1
                knight(x1,y1, x, y-1, n1+1, n2, r+x1[x][y-1])

        if ch(x,y+1,n2):
            if y1[x][y+1]==-1:
                y1[x][y+1]=1
                knight(x1,y1, x, y+1, n1+1, n2, r+x1[x][y+1])
    return

x1 = [['a','b'],['x','y']]
tm=[[-1,-1],[-1,-1]]
n2=2
knight(x1,-1,1,1,1,n2)
print(ans)



