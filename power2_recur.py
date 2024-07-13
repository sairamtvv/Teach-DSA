
def pow2(i):
    if i ==0 or i==1:
        return 1

    prev = pow2(i//2)
    curr = 2*prev
    print(curr)
    return curr

pow2(139)

