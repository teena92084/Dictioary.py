# a={"t":2,"k":5,"p":6,"r":"python"}
# s=0

# for i in a.values():
#     if type(i)==int:
#         s=s+i
    
# print(s)









# n=int(input('enter the number of data you need in your dict: '))
# i=0
# dict={}
# while i<n:
#     Name=input('enter the name: ')
#     dict2={}
#     num=int(input('enter the num of sub: '))
#     j=0
#     while j<num:
#         subN=input('enter the subject name: ')
#         marks=int(input('enter the marks obtained in the sub: '))
#         dict2[subN]=marks
#         j+=1
#     dict[Name]=dict2
#     i+=1
# print(dict)




# a={"name":"teena","age":20,"city":"jaipur"}
# if a["age"]>30:
#     a.pop("age")
# print(a)

    



# dic={"s":3,"a":{"t":["tina","pooja","piya"]}}

# for item in dic:
#     if type(dic[item])==dict:
#         for item2 in dic[item]:
#             if type(dic[item][item2])==list:
#                 print(dic[item][item2])




# a={"s":4000,"t":4000,"p":4000}
# l=[4000,4000,4001]
# b=l[0]
# for x in a.values():
#     if x==b:
#         print("true")  
#     else:
#         print("false")






# a = {"t": 5, "s": 2, "p": 3}
# c = []
# b = []
# for i ,x in a.items():
#     if type(i) == str:
#         c.append(i)
# for j, y in a.items():
#     if type(y) == int:
#         b.append(y)


# print(c)
# print(b)



# b={"t":3,"k":4,"s":2}
# f=1
# for i in b:
#     f=f*b[i]
# print(f)    






# a={"t":2,"k":5,"p":6,"r":"python"}
# s=0

# for i in a.values():
#     if type(i)==int:
#         s=s+i
    
# print(s)





# a={1:2,2:4,3:3,4:3}
# n=int(input("enter the key"))
# if n in a:
#     a.pop(n)
#     print(a)
# else:
#     m=int(input("enter the value"))
#     a[n]=m
#     print(a)




# dictionary value or key ka sum

# a={1:5,2:2,3:3,4:8}
# b=[]
# s=0
# s2=0
# r=[]
# # c=[]
# for i in a:
#     c=a[i]
#     s=s+c
#     c=i
#     s2=s2+c
# b.append(s)
# r.append(s2)
# print("value",b)
# print("key",r) 

# 
#    

# nested dictionary ki value or key ka  sum

# a={3:{1:5,2:2,3:3,4:8}}
# s=0
# s1=0
# for i in a:
#     for x in a[i].values():
#         s1=s1+(x)
#         s=s+(i)
# print(s) 
# print(s1)       





# v={"annu":2,"sannu":4,"teena":"pooja",}
# s=[]
# x=[]
# for i in v:
#     a=v[i]
#     s.append(a)
#     b=i
#     x.append(b)
    
# print(s)
# print(x)   
# 
# 
# 
#  

# short krna asendin or desindind order

# d1={2:1000,3:100,4:90,500:600000}
# li=[]

# for i in d1:
#     li.append(d1[i])
#     for i in range(len(li)):
#         for j in range(len(li)):
#             if li[i]<li[j]:
#                 li[i],li[j]=li[j],li[i]
# print(li)                
# n={}  
# for h in li:
#     for l in d1:
#         if d1[l]==h:
#             n.update({l:h})
# print(n)





###ek k bad ak key value nikalna

# a={"fist1":{"teena":"kanawae","ppoja":"rathore"},
# "fist2":{"annu":"jitu","sannu":"ajay"}
# }
# for i in a:
#     print(i)
#     for j in a[i]:
#         # print(j,a[j][i])
#         print(j,a[i][j])




#max value nikalna mimum####

# my={"t":3,"y":6,"p":9,"k":5,"tina":90,"r":1}
# a=[]
# for i in my.values():
#     a.append(i)
# b=[] 
# c=[] 
# for i in  range(1):
#     b.append(max(a))
#     c.append(min(a))
    
# print(b) 
# print(c)   


# a={"fist1":["tina","meena","ankita"],"second":["ppoja","karina,","aaru"]}
# c=0
# for i in a:
#     for j in a[i]:
#         c=c+1
# print(c)        



# a={"k1","k2","k3","k4"}
# c={}
# b=c.fromkeys(a,6)
# print(b)



####conver dictionary to list of list

# marks ={"teena":3,"radh":4,"parkash":"tina","khusubhu":7}
# c=[]
# for i in marks.items():
#     c.append(list(i) )   
# print(c)    



# a=[2,3,3,2,5,1,9,1]
# dictt={}
# for i in a:
#     dictt.update(i)
# print(dictt)


#convrt to dictionaty to list


# a={"teena":"k","pooja":"r","sannu":"s"}
# v=[]
# for i in a:
# # for i in a.values() :       
#     v.append(list(a[i]))
#         # v.append(i)

# print(v)





# a=[["teena","k","pooja"],["r","sannu"]]
# b={}
# for i in a:
#     b.update({i[0]:i[1]})
# print(b)    





# key=["red","green","yellow",]
# value=["ff00","ooo8","kiya"]
# b={}
# i=0
# while i <len(key):
#     b.update({key[i]:value[i]})
#     i=i+1
# print(b)    




# d={"tina":["pooja","kitt","temsa"]}
# for i in d:
#     print(i)
#     for j in d[i]:
#         print(j)





# d={"tina":3,"i":{"ja":["pooja","kitt","temsa"]}}
# for i in d:
#     print(i)
#     if type(d[i])==dict:
#         # print(d)
#         for item2 in d[i]:
#             if type(d[i][item2])==list:
#                 print(d[i][item2])

        
# 


# d={"tina":3,"i":{"ja":["pooja","kitt","temsa"]}}
# for i in d:
#     print(i)
#     if type(d[i])==dict:
#         for j in d[i]:
#             if type(d[i][j])==list:
#                 print(d[i][j])



#duplicst remove krna


# a={"teena":3,"P":4,"pink":23,"teena":4,"aarti":23}
# v=[]
# # v={}
# for i in a.items():
#     if i not in v:
#         v.append(i)
#         # v.update({i[0]:i[1]})
# print(v)        






# m=int(input("enter the no you want"))
# i=0
# b={}
# while i<m:
#     name=(input("enter the name" ))
#     marks=int(input("enter the maeks"))
#     b[name]=marks
#     i=i+1
# print(b)    




# short krna asendin or desindind order

# # d1={2:1000,3:100,4:90,500:600000}
# li=[]

# for i in d1:
#     li.append(d1[i])
#     for i in range(len(li)):
#         for j in range(len(li)):
#             if li[i]<li[j]:
#                 li[i],li[j]=li[j],li[i]
# print(li)                
# n={}  
# for h in li:
#     for l in d1:
#         if d1[l]==h:
#             n.update({l:h})
# print(n)






# d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# a=[]
# for i in d:
#         a.append(d[i])
#         for i in range(len(a)):
#                 for j in range(len(a)):
#                         if a[i]>a[j]:
#                                 a[i],a[j]=a[j],a[i]
# print(a)
# n={}
# for h in a:
#         for l in d:
#                 if d[l]==h:
#                         n.update({l:h})
# print(n)                        



# a={"k1","k2","k3","k4"}
# v={}
# g=v.fromkeys(a,29)
# print(g)


# d1={"a":100,"b":200,"c":300,"d":300}
# d2={"a":300,"b":200,"c":100,"e":400}
# for i in d1:
#         if i in d2:
#                 d2[i]=d1[i]+d2[i]
#         else:
#                  d2[i]=d1[i] 
# print(d2)                       



# a="w3resourece"
# b={}
# for i in a:
#         if i not in b:
#                 b[i]=b[i]=1
#         else:
#                 b[i]=b[i]+1
# print(b)                        
                


# n=(input("enter the key"))
# if n=="{}":
#         print("dictionary is ampti")
# else:
#         print("dicti is not empty")        























# a={1:2,2:4,3:3,4:3}
# n=int(input("enter the key"))
# if n in a:
#     a.pop(n)
#     print(a)
# else:
#     m=int(input("enter the value"))
#     a[n]=m
#     print(a)
