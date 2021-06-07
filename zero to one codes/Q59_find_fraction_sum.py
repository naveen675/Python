



if __name__ == '__main__':
    #n = int(input())
    print(round((sum(i/(i+1) for i in range(1,int(input())+1))),2))

                        ## OR  ##

    print(round(sum(map(lambda i:i/(i+1),[*range(1,int(input())+1)])),2))


