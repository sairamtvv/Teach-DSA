def recursiveprint(n):
    if n<1:
        print("n is less than 1")
    else:
        recursiveprint(n-1)
        print(n)

def poweroftwo(n):
    if n==0:
        return 1
    else:
        power = poweroftwo(n-1)
        print(power*2)
        return power * 2

def twotopowerit(n):
    power = 1
    i=0
    while i< n:
        power = power * 2
        i =i+1
    print(power)
    return power

if __name__ == "__main__":
    #recursiveprint(4)
    #poweroftwo(3)
    twotopowerit(4)