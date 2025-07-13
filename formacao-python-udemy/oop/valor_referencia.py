lst1 = 10
lst2 = lst1 # cópia por valor
print(lst1)

lst1 = [1,2,3]
lst2 = lst1 # cópia por referência, pois é uma lista
lst2.append(10)
print(lst1)