n,*l=map(int,open(0).read().split())
M=N=n;v=w=c=0;p=l[0]
for i in l:
    v+=(x:=N//i);N-=x*i
    if i>p:
        c=max(c+1,1)
        if c>2:M+=w*i;w=0
    elif i<p:
        c=min(c-1,-1)
        if c<-2:w+=(x:=M//i);M-=x*i
    else:c=0
    p=i
N+=v*i;M+=w*i
print(['SAMESAME','BNP','TIMING'][(N>M)+2*(N<M)])