def per(inp,op):
    if len(inp)==0:
        print(op)
    for i in range(len(inp)):
        ch=inp[i]
        left_substr=inp[0:i]
        right_substr=inp[i+1:]
        rest=left_substr+right_substr
        per(rest,op+ch)
inp="heye"
op=""
per(inp,op)
'''
heye
heey
hyee
hyee
heey
heye
ehye
ehey
eyhe
eyeh
eehy
eeyh
yhee
yhee
yehe
yeeh
yehe
yeeh
ehey
ehye
eehy
eeyh
eyhe
eyeh
'''