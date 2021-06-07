

def recur(n):
    if n==0:
        return 0
    return recur(n-1)+100


if __name__ == '__main__':

    #print(recur(int(input())))

    f = lambda x: 0 if x==0 else f(x-1)+100

    print(f(int(input())))
