# Program to check whether the shuffled string is a valid shuffle of the other two strings

def validShuffle(s1,s2,shuffledstr):
    if len(s1)+len(s2)!=len(shuffledstr):
        return False
    newstr=s1+s2
    newstr=sorted(newstr)
    shuffledstr=sorted(shuffledstr)
    if newstr!=shuffledstr:
        return False
    return True
s1="abcd"
s2="hjik"
shuffledstr="ahijkbdc"
print(validShuffle(s1,s2,shuffledstr))
#True