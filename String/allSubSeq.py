
def allSubseq(inp,op,i,n):
    if i==n:
        print(op)
    else:
        allSubseq(inp,op,i+1,n)
        allSubseq(inp,op+inp[i],i+1,n)
inp="abcs"
op=""
i=0
n=len(inp)
allSubseq(inp,op,i,n)
'''

s
c
cs
b
bs
bc
bcs
a
as
ac
acs
ab
abs
abc
abcs''' 
