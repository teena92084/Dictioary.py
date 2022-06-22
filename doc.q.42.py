# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# print("Original Dictionary:")
# print(marks)
# print("Marks greater than 170:")
# result = {key:value for (key, value) in marks.items()

# if value >= 170}
# print(result)



# b={}
# for i in marks .values():
#     if i>170:
#         print(i)

# r={key:value for (key, value)in marks.items()if value>=170}






# b={}
# for key,value in marks.items():

#     if value<=170:
#         print("d")
        
#         print(key,value)
      



# marks ={"teena":3,"radh":4,"parkash":5,"khusubhu":7}
# v={}
# for i in marks:
#     if marks[i]>4:
        
#         print(i,marks[i])



a={"v":[1,2,3],"vi":[4,6,8],"vii":[10,12]}
c={}
for i in a:
    for j in a[i]:
        if j%2==0:
            c.update({j:i})
print(c)            