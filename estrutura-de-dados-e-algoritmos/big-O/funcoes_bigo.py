from math import log
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,10,100)

labels = ['Constant','Logarithmic','Linear','Log linear','Quadratic','Cubic','Exponential']
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3,2**n]

plt.figure(figsize=(10,8))
plt.ylim(0,100)
for i in range(len(big_o)):
    plt.plot(n,big_o[i],label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')
#plt.savefig('graficos.png')

#Constant - O(1)
lista = [1,2,3,4,5]
def constant(n):
    print(n[0])
constant(lista)

#Linear - O(n)
def linear(n):
    for i in n:
        print(i)
linear(lista)

#Quadratic - O(n^2) - polynomial
def quadratic(n):
    for i in n:
        for j in n:
            print(i,j)
quadratic(lista)

#Combination - O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n) -> O(n)
def combination(n):
    # O(1)
    print(n[0])

    # O(5)
    for i in range(5):
        print('test ', i)

    # O(n)
    for i in n:
        print(i)

    # O(n)
    for i in n:
        print(i)

    # O(3)
    print('Python')
    print('Python')
    print('Python')

combination(lista)