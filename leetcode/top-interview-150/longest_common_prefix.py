'''
https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150
'''

strs = ["flower","flow","flight"]
lista = []
i = 0
while i < len(strs):
    for str in strs[:i+1]:
        if strs[i][:1] in str:
            lista.append(strs[i][:1])
    print(strs[i][:1])
    print(strs[:i+1])
    i += 1

print(lista)

'''
1.pegar as strings do array
2.verificar se tem as letras em todas as palavras contidas no array
3.verificar se a próxima letra tem em todas as strings do array
'''