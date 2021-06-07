

def even_num(a,b):
    for i in range(a,b+1):
        if i%2 == 0:
            if(i==b):
                print(str(i),end='')
            else:
                print(str(i)+',',end='')



if __name__ == '__main__':
    
    #even_num(1000,30000000)
    a,b= input().split(',')
    l = [*range(int(a),int(b)+1)] #will generate a list of elements from a to b
    print(','.join(list(map(str,(filter(lambda a:a%2==0,l))))))  