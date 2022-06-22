# 43.Write a Python program to create a dictionary grouping a sequence of key-value pairs
# into a dictionary of lists.
# Original list:

# colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# # 
# Sample Output:
# 'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}



# colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# r={}
# for x,y in  colors:
#     r.setdefault(x,[]).append(y)
# print(r)    

# d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# a,b=d.values()
# l=[]
# for i in range(len(a)):
#     c={}
#     for j in d:
#         c.update({j:d[j][i]})

#     l.append(c)
# print(l) 
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]
# from re import I


# a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['ZacharySimon']}
# # b={}
# # c=[]
# for i in a:
#     c=[]
#     b={}
#     for j in a[i]:
#         b.update({j:a[i][j]})
#     c.append(b)
# print(c)


# {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
# d1={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# # {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
# li=[]
# for i in d1:
#     li.append(d1[i])
#     for i in range(len(li)):
#         for j in range(len(li)):
#             if li[i]>li[j]:
#                 li[i],li[j]=li[j],li[i]
# new={}
# for h in li:
#     for l in d1:
#         if d1[l]==h:
#             new.update({l:h})
# print(new)                        














