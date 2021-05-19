
####### Using join #######
# def rm_duplicate(s):
#     s = set(s)
    
#     return " ".join(s)


# def rm_duplicate(s):
#     s = s.split(" ")
#     for word in s:
#         if s.count(word)>1:
#             s.remove(word)
#     return " ".join(sorted(s))

# def rm_duplicate(s):
#     s = sorted(s.split(" "))
#     item = iter(s)
#     next(item)
    
#     for word in s:
#         try:
#             if word == next(item):
#                 s.remove(word)
#         except StopIteration:
#             break
#     return " ".join(s)




if __name__ == '__main__':

##### single line ########
    print(sorted((list(set(input().split(" "))))))


    #print(rm_duplicate(input()))


    # s = [input().split(" ")
    # print(s)
