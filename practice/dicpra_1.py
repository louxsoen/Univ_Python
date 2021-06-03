all = []

for i in range(5):
    name = str(input("이름 : "))
    num =int(input("분반 : "))
    a= {'이름':name, '분반':num}
    all.append(a)
    

a.values()
print(all)