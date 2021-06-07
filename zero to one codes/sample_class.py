class test:
    def __init__(self,s):
        self.s = s
    
    def str_upper(self):
        return self.s.upper()

    

t = test(input("Enter String"))
print(t.str_upper())
