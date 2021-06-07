from collections import Counter
from pprint import pprint


# if __name__ == '__main__':
#     s=input()
#     words = sorted(list(set(s.split(' '))))
#     for word in words:

#         print(word+":"+str(s.count(word)))


#### Method 2 ####

# ss = input().split()
# print(ss)
# dict = {}
# for i in ss:
#     i = dict.setdefault(i,ss.count(i))  # setdefault() function takes key & value to set it as dictionary.

# dict = sorted(dict.items())               # items() function returns both key & value of dictionary as a list
#                                           # and then sorted. The sort by default occurs in order of 1st -> 2nd key
# for i in dict:
#     print("%s:%d"%(i[0],i[1]))
    

####   Method 3 ####

# s = input().split()

# c = Counter(s)
# c = sorted(c.items())

# for i in c:
#     print(i[0] +':'+ str(i[1]))

#print(c)

### Method 4 ###

s = input().split()

pprint({i:s.count(i) for i in s})




