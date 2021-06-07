
class gen:


    def multiple(n):

        for i in range(0,int(n/7)+1):
            yield i*7

    

for i in gen.multiple(int(input())):
    print(i)