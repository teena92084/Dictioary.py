a=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,
'Zachary Simon', 'VII']]
b={}
for i in a:
    b.update({i[0]:i[1:]})
print(b)