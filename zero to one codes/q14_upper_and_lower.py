
if __name__ == '__main__':
    
    l = list(input())
    print("UPPER CASE "+ str(len([i for i in l if i.isupper()])))
    print("LOWER CASE "+ str(len([i for i in l if i.islower()])))


    