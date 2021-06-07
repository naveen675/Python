

# def two_dimension(n,m):
    
#     o=[]
#     for i in range(0,n):
#         l=[]
#         for j in range(0,m):
#             l.append(i*j)
#         o.append(l)
#     return o

# def two_dimensional(n,m):
#     o=[[i*j for j in range(m)] for i in range(n)]
#     return o

# print(two_dimensional(3,5))

# s = [input().split(',')]
# a =','.join(s.sort())
# print(a)



l = []
s = input() 
while s:
    l.append(s.upper())
    s = input()
a = "\n".join(l)
print(a)



