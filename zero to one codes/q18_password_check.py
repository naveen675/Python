import re




if __name__ == '__main__':

    pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")
    print(','.join([i for i in input().split(',') if pattern.fullmatch(i)]))
    #print(','.join([i for i in input().split(',') if len(i) >=6 and  len(i) <= 12 and re.search('[a-z]',i) and re.search('[A-Z]',i) and re.search("[$#@]",i)]))

