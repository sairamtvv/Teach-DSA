def inttostr(i):
    digits="0123456789"
    if i ==0 :
        print(0)

    result =""
    while i>0:
        result = digits[(i%10)] + result
        i = i//10

    print(result)
inttostr(-21354)