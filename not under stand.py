

  


# # a=["a","b","c"]
# # b=(1,2,3)

# # # a.extend(b)

# # i=0
# # while i<len(a):
# #     c=[]
# #     d=c+i
# # print(d)






# #  39.Write a Python program to filter a dictionary based on values.
# # # Original Dictionary:
# # # {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# # # Marks greater than 170:
# # # {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}


# # sum={'Cierra Vega': 175, 'Alden Cantrell': 180, "Kierra": 165, 'Pierre Cox': 190}
# # b=sum.pop("kierra Gentry")
# # # # print(b)
# # # print(sum.pop("kierra"))
# # print(sum)
# # print







  


# # Write a program to print 'exists' if entered key already exists in the dictionary and print 'not exists' if the entered key does not exist.
# # Example :-
# # Code Example

# # dict1={“name”:”Raju”, “marks”:56}
# # Note :-

# # If input is “name” then output will be “exist”

# # If input is “class” then output will be “not exists”



# # Take a list having dictionary elements as shown below (Sample Data) and then store all the unique values into a list and print.
# # Example :-
# # Input :-
# # Code Example

# # [
# #   {"first":"1"}, 
# #   {"second": "2"}, 
# #   {"third": "1"}, 
# #   {"four": "5"}, 
# #   {"five":"5"}, 
# #   {"six":"9"},
# #   {"seven":"7"}
# # ]
# # Output :-

# # ['2', '7', '9', '5', '1']



# #}



# # 



# #




# # 








# # Write a program to print the top 3 highest values of a given dictionary.
# # Example :-
# # Code Example

# # my_dict = {
# # 'a':50, 
# #  'b':58,
# #  'c': 56,
# #  'd':40,
# #  'e':100, 
# #  'f':20
# #  }
# # expect result:-['e','b','c']




# # d ={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# # for k in d.keys():
# #     d [k] = [i for i in d[k] if i%2 !=0]
# # print(d)


# # num=int(input("enter the number room no"))
# # b=[]
# # # b=["teena","pooja","lia"]
# # i=0
# # while i<num:
# #     name=input("enter the name")
# #     # while b>2:
# #         # print(b)
# #     b.append(name)
# #     i=i+1
# # print(b)    










# # rno=int(input("enter the number of room"))
# # # name=(input("enter the girls name "))
# # # if rno==1(["pooja,rina,giya"]) or rno==2(["t","k"]):
# # if rno==1:
# #     print("pooja,lina,teena,seena,rina->room no1")
# #     if rno==2:
# #         print("manu,punam,swati,radha,ws")
# #         if rno==3:
# #             print("shrya,kiya,pooma,teena,radha")
# #             if rno==4:
# #                 print("pooja,ranai,insha","teena","jiya->room no.4")
# #             else:
# #                 print("t","k","r","s","p")        
# #         else:
# #             print("l","piriya","t","k","p") 
                  
# #     else:
# #         print("asha")   
# # else:
# #     print("piya")                   

# # room=open("rooom shuffling.text","w")
# # br=room.write("teena","piya","krina","pooja")

# # import random

# a=["teena","pooja","rani","tunja","kashose","punoom","nikit","aaarti","piya","neetu","shrya","ankita","bhgyeshree","megha"]
# room=[401,402,403,405,406]
# user=int(input("how mani girls you want in room->"))
# i=0

# # b=[]
# while i<len(a):
#     j=0
#     c=[]
#     while j<user:
#         c.append(a[j])
#         j=j+1
#     # b.append(c)
#     i=i+1
# print(c)
# # i=i+1
# # print(b)       












# rooms=[401,402,403]
# a=["teena","pooja","rani","tunja","kashose","punoom","nikit","aaarti","piya","neetu","shrya","ankita","bhgyeshree","megha","susuti","riya","prinka","tina","alpna","radha","pyal","varsha"]
# n=int(input("enter the num"))

# if n<=len(a)//len(rooms):
#     i=0
#     b=[]
#     l=[]
#     while i<len(a):
#         b.append(a[i:i+n])
#         i+=n
#     my_dict={}    
#     i=0
#     while i<len(rooms): 
#         my_dict[rooms[i]]=b[i]
#         i=i+1

#     print(my_dict) 
# else:
#     print("pleas enter correct no ->",len(a)//len(rooms))    





#
#

#







# 
# c

# Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language':
# 84}, {'Science': 95, 'Language': 80}]



# a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# b={}
# for i in a:
#     for j in a[i].values():
#         c=({i[0:7]:i[2]})
#     b.update(c)
# print(b)    







        
# a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

# for k in a :
#     a[k]=[i for  i in a[k] if i%2==0]
    
# print(a)


# a={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# for y in a:
#     a[y]=[i for i in a[y] if i%2==0]
# print(a)      



# dicit={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}



# dicit={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b={}
# for val in dicit.values():
#     b[val]=len(val)
# print(b)    

# s={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# b={}
# for i in s.values():
#     b[i]=len(i)
# print(b)    


# a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b=[]
# for i in a.items():
#     b.append(i)
# print(b)    





# dicit={1: 20, 2: 2, 3: 3,5:[ 4: 3, 5: 2]}
# s=0
# for  x in dicit:
#     for j in dicit[x].values():
#         s=s+(dicit[j])
# print(s)    
    

# a={"tina":["sub","syn","piya"],"pooja":["ti","liya","kiyo"]} 
# c=0
# for i in a:
#     for j in range(len(a[i]) ):
#         c=c+j
# print(c)         




# a=["pooja","piya","usha","riya"]
# b=[1,2,3,5]
# i=0
# b={}
# while i<len(a):
#     b.update({a[i]:b[i]})
#     i=i+1
# print(b)    


# n=int(input("enter the number"))
# b={}
# for i in range(1,n):
#     b[i]=i**2
#     # b.update(i) 
# print(b)       



# a='w3resource'
# b={}
# for i in (a):
#     b[i]=b.get(i,0)+1

# print(b)



# a={"t":["p","r",],"p":["pooja","liya"]}
# c=0
# for i in a:
#     for x in range(len(a[i])):
#         c=c+1
# print(c)        









# a={1: 'red', 2: 'green', 3: 'black'}
# b={ 4: 'white', 5: 'black'}
# c={'Math':81, 'Physics':83, 'Chemistry':87}

# # c=a.copy()
# # c.update(b)
# # print(c)
# s={}
# for i in (a,b,c):
#     s.update(i)
# print(s)




# my_dicit={"a":1,"b":2,"p":3}
# # my_dicit.pop("a")
# # print(my_dicit)
# if "a" in my_dicit:
    
#     del my_dicit["a"]
    
# print(my_dicit)







# dic={"s":["tina","pooja","piya"]}
# for i in dic:
#     for j in dic[i]:
#         print(j)







# dic={"s":3,"a":{"t":["tina","pooja","piya"]}}

# for item in dic:
#     if type(dic[item])==dict:
#         for item2 in dic[item]:
#             if type(dic[item][item2])==list:
#                 print(dic[item] [item2])













#
# 
     

# n=int(input('enter the number of data you need in your dict: '))
# i=0
# dict={}
# while i<n:
#     Name=input('enter the name: ')
#     dict2={}
#     num=int(input('enter the num of sub: '))
#     j=0
#     while j<num:
#         sub=input('enter the subject name: ')
#         marks=int(input('enter the marks obtained in the sub: '))
#         dict2[sub]=marks
#         j+=1
#     dict[Name]=dict2
#     i+=1
# print(dict)






# a={"name":"teena","age":20,"city":"jaipur"}
# if a["age"]>30:
#     a.pop("age")
# print(a)








# a={"t":2,"k":5,"p":6,"r":"python"}
# s=0

# for i in a.values():
#     if type(i)==int:
#         s=s+i
    
# print(s)














# a={"s":4000,"t":4000,"p":4000}
# l=[4000,4000,4001]
# b=l[0]
# for x in a.values():
#     if x==b:
#         print("true")
#     else:
#         print("false")






# a={"name":"teena","age":20,"city":"jaipur"}
# if a["age"]>30:
#     a.pop("age")
# print(a)






# d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# print("original dictionary",d)
# b={}
# b.update(sorted(d.items()))
# print("ascending order",b)






# b={"t":3,"k":4,"s":2}
# f=1
# for i in b:
#     f=f*b[i]
# print(f)    







# import json

# dict1 ={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# }

# # myfile.json ek json file hai jisme hum uper wala python object dump or store kerayge.
# # Code Example

# out_file = open("myfile.json", "w")
  
# json.dump(dict1, out_file,indent=3)
  
# out_file.close()


# # Dumps() :- Dumps() method python objects ko json file mai string ke format mai store karene ki liye use hota hai. String format mai hum python objects(dictionary) ko tab store karate hai jab hume bo objects print karane ho ya phir parse karene ho.

# # Example:-
# # Code Example


# # import json

# # a={‘lalalala’: 3}
# # mystring = json.dumps(a)
# # print(mystring)





# import json

# a={"lalalala": 3}
# mystring = json.dumps(a)
# print(mystring)





# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(x["age"]) 





# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y) 





# import json
# ####"json conver to python dictionary"
# a='{"name": "David", "class": "I", "age": 6}'
# # # print()
# # p=json.loads(a)
# # print(p)

# j=json.dumps(a,indent=10)
# print(j)


# import json
# age=20
# salarya=300.40
# print(json.dumps(salarya))
# name="teena"
# print(json.dumps(name))

# print(json.dumps(a,separators=("/",".")))




# import json

# a={'lalalala': 3}
# mystring = json.dumps(a)
# print(mystring)



# a={1:2,2:3,3:3,4:4}
# n=(input("enter the key"))
# if n in a:
#     a.pop(n)
#     print(a)
# else:
#     v=int(input("enter  value")) 
#     a[n]=v 
#     print(a)  





# b={1:2,6:3,2:4,8:3}
# i=0
# a=b[0]
# b=b+1
# print(b)