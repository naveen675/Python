from collections import Counter


s = 'abcdefgabc'

s = dict(Counter(s))
for key,value in s.items():
    print(key+','+str(value))