def perm(inp, op):
    hm = {}
    if len(inp) == 0:
        print(op)
    for i in range(len(inp)):
        if inp[i] in hm:
            continue
        hm[inp[i]] = 1
        perm(inp[:i] + inp[i+1:], op + inp[i])


inp = "pep"
op = ""
# perm(inp,op)
'''
pep
ppe
epp'''


def find_permutation(S):
    # Code here
    res = set()

    def permute(arr, l, r):
        nonlocal res
        if l == r:
            res.add(''.join(arr))
            return
        for i in range(l, r):
            arr[i], arr[l] = arr[l], arr[i]
            permute(arr, l+1, r)
            arr[i], arr[l] = arr[l], arr[i]

    permute(list(S), 0, len(S))
    return sorted(res)
