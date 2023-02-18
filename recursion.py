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

def gcd(a,b):
    if a==0 or b==0:
        return max(a,b)
    else:
        mod = max(a,b) % min(a,b)
        print(mod)
        return gcd(min(a,b), mod)
def fib(n):
    if n in [0,1]:
        return 1
    else:
        return fib(n-1) + fib(n-2)



def rev(a:str):
    if len(a)==1:
        return a
    else:
        c = rev(a[1:])
        return c + a[0]


def dec_to_bin(n):


    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        quo = int(n / 2)

        k = str(dec_to_bin(quo))
        print(quo, k+ str(n%2))
        return k + str(n%2)


# 4 - 2  0
# 2 1   0
# 1     1
#
# 5 2 1
# 2 1 0
#
# 0 0 0
#
# 1 0 1

def dec_to_bin2(n):
    if n in [0,1]:
        return n
    else:
        quo = int(n/2)
        k = dec_to_bin2(quo)
        print(str(k)+str(n%2))
        return str(k)+str(n%2)


# abccba  1) remove 1st and last , check forst char == last charr
#
# abcdcba

def ispalindrome(k):
    if len(k)==1:
        print(True)

    elif len(k)==2 and k[0]==k[1]:
        return (True)
    else:
        if k[0] == k[-1]:
            return ispalindrome(k[1:-1])

        else:
            return False
# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])


def isPalindrome(k):
    if len(k) ==0:
        return True
    if k[0]!= k[-1]:
        return False
    return isPalindrome(k[1:-1])


def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True

# if there is no odd number in array return False
#
#

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if cb(arr[0]) == False:
        return someRecursive(arr[1:], cb)
    else:
        return True


if __name__ == "__main__":
    #recursiveprint(4)
    #poweroftwo(3)
    #twotopowerit(4)
    # a,b = 48, 18
    # num_gcd = gcd(a,b)
    # lcm = (a*b)/num_gcd
    # print(lcm)
    # for i in range(10):
    #     print(fib(i))
    #print(rev("xyzabcdef"))
    #print(dec_to_bin2(8))
    #
    # print(isPalindrome('awesome'))  # false
    # print(isPalindrome('foobar'))  # false
    #print(isPalindrome('tacocat'))  # true
    # print(isPalindrome('amanaplanacanalpanama'))  # true
    # print(isPalindrome('amanaplanacanalpandemonium'))  # false

    print(someRecursive([1, 2, 3, 4], isOdd))
    print(someRecursive([4, 6, 8, 9], isOdd))  # true
    print(someRecursive([4, 6, 8], isOdd))  # false