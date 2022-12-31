def recursiveprint(n):
    if n<1:
        print("n is less than 1")
    else:
        recursiveprint(n-1)
        print(n)

if __name__ == "__main__":
    recursiveprint(4)