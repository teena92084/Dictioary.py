# my_d={"dict1":{"t":"k","maya":"lila"},"dicit2":
# {"s":"k",}
# }

# for i in my_d:
    
#     for j in my_d[i]:
#         print(my_d[i][j])









# my_d={"dict1":{"t":"k","maya":"lila"},"dicit2":
# {"s":"k"}
# }
# b={}
# for i in my_d:
    
#     for j in my_d[i]:
#         # print(j,my_d[i][j])
#         b.update({j:i})
# print(b)




# my_d={"dict1":{"t":"k","maya":"lila"}}

# b={}
# for i in my_d:
#     for j in my_d[i]:
#         b.update({j:i})
# print(b)        




# a={
#     "di":{"t":"pooja","k":"kanawar"},
#     "r":{"teena":"piya","riya":"siya"},


#     "rd":{"p":"rina","ty":"p"},
#     "t2":{"liya":"li","kiya":"kni"}
# }



# for i in a:
#     for j in a[i]:
#         print(a[i][j])


        








#####dictionary k under  user input laker na,name append krna or marks

           

# n=int(input('how mani name you enter the dictionary : '))
# i=0
# dict={}
# while i<n:
#     Name=input('enter the name: ')
#     dict2={}
#     num=int(input('enter the no of sub: '))
#     j=0
#     while j<num:
#         sub=input('enter the subject name: ')
#         marks=int(input('enter the marks obtained in the sub: '))
#         dict2[sub]=marks
#         j+=1
#     dict[Name]=dict2
#     i+=1
# print(dict)


      




#####nested dictionay k under list k element nikalna

# dic={"s":3,"a":{"t":["tina","pooja","piya"]}}
# dic={"s":3,"a":{"t":["rina","pooja","piya"]}}
# for item in dic:
#     if type(dic[item])==dict:
#         for item2 in dic[item]:
#             if type(dic[item][item2])==list:
#                 print(dic[item][item2])

