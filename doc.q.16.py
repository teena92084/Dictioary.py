# 
# Write a Python program to remove duplicates from Dictionary.


student_data = {
    'id1':{'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
},
    'id2':{'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
},
    'id3':{'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
},    
    'id4':{'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
}
}
r={}
for key,Value in student_data.items():
    if Value not in r.values():
        r[key]=Value
print(r)   


     

# print(student_data)
# 'id2': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['David']}, 'id4':
# {'subje
# ct_integration': ['english, math, science'], 'class': ['V'], 'name': ['Surya']}, 'id1':
# {'subject_integration'
# : ['english, math, science'], 'class': ['V'], 'name': ['Sara']}}