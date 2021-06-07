from functools import reduce

def cal_let_dgt(s):
    s = list(s)
    ltr = 0
    dgt=0
    for i in s:
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 95 and ord(i) <= 122):
            ltr=ltr+1
        elif ord(i) >= 48 and ord(i) <= 57:
            dgt=dgt+1

    print("Letters "+str(ltr))
    print("Digits "+str(dgt))
    

def check_letter(i):
    if i.isalpha():
        return i
def check_number(i):
    if i.isdigit():
        return i

def accumulator(acc,item):
    if item.isalpha():
        acc[0] = acc[0]+1
    elif item.isdigit():
        acc[1] = acc[1]+1   

    return acc


if __name__=='__main__':

    # cal_let_dgt(input())
    # ltr=0
    # dgt=0
    

    # Using filter

    #l = list(input())
    #r(len(list(filter(check_letter,l)  ) ) ) )
    # print(list(filter(check_number,l)))
    # print("Number "+ str(len(list(filter(check_number,l)  ) ) )  ) 
    # print("Letter "+ str(len(list(filter(check_letter,l)  ) ) )  )
    # 
    # Using List comprehension
    #  
    l = list(input())
    print("LETTERS: " + str(len([i for i in l if i.isalpha()])))
    print("DIGITS "+ str(len([i for i in l if i.isdigit()])))

 


    #print("Letter : {0}\nNumber : {1}".format(*reduce(accumulator,list(input()),[0,0])))