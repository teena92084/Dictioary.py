# # Q51.Write a Python program to filter even numbers from a given dictionary values.
# # Original Dictionary:
# # a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# # Filter even numbers from said dictionary values:
# # {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}



# d ={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for k in d.keys():
#     d [k] = [i for i in d[k] if i%2 ==0]
# print(d)


# a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# # Filter even numbers from said dictionary values:
# #o/p {'V': [], 'VI': [], 'VII': [2]}


# d={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# for k in d.keys():
#     d[k]=[i for i in d[k] if i%2==0]
# print(d)    










# a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for i in a:
#     a[i]=[i for i in a[i] if i%2==0]
# print(a)    




# a={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# for i in a:
#     a[i]=[i for i in a[i] if i%2==0]
# print(a)    



# a={"v":[1,2,3],"vi":[4,6,8],"vii":[10,12]}
# c={}
# for i in a:
#     for j in a[i]:
#         if j%2==0:
#             c.update({j:i})
# print(c)  