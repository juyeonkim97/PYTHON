import sys
def DFS(L,s):
    global cnt
    if(L==m):
        for j in res:
            print(j,end=" ")
        print()
        cnt+=1
        return
        
    else:
        for i in range(s,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1,i+1)
                ch[i]=0

n,m=map(int,input().split())
cnt=0
ch=[0]*(n+1)
res=[0]*m
DFS(0,1)
print(cnt)

     

