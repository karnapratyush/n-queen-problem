# assume a board as a list having each box assigned as 0 initially
#asking the size of the board
n=int(input("enter the value of n for n*n size board:  "))
a=[[0 for i in range(n)]for j in range(n)]


#to check if we can put on a certain row and column
def check(a,col,row):
    for i in range(n):
        if a[col][i]==1:
            return False
        if a[i][row]==1:
            return False
        for j in range(n):
            if j-i==col-row and a[j][i]==1:
                return False
            if j+i==col+row and a[j][i]==1:
                return False
    return True

#if check returns true then we will try to assign queen
def assign_queen(a,col,i):
    if col<n-1:
        while i<n:
            if check(a,col,i):
                a[col][i]=1
                return assign_queen(a,col+1,0)
            i=i+1
    elif col==n-1:
        for h in range(n):
            if check(a,col,h):
                a[col][h]=1
                return ( a)
     #backtracking
    t=a[col-1].index(1)
    a[col-1][t]=0
    return assign_queen(a,col-1,t+1)



assign_queen(a,0,0)
for i in range(len(a)):
    print(a[i])
