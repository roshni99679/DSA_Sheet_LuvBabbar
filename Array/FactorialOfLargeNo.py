
def factorial(N):
        #code here
        a=[]
        i=N
        fact=1
        while i>0:
            fact*=i
            a.append(i)
            i-=1
        return fact,a 
print(factorial(5))