'''
https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150
'''

strs = ["flower","flow","flight"]
letras = ""
letras_comum = ""
x = 0
for i in range(len(strs)):
    if strs[i] == strs[0]:
        letras = strs[i][:1]
    if strs[i] != strs[0]:
        if letras == strs[i][:1]:
            letras_comum = strs[i][:1] 

'''
1.pegar as strings do array
2.verificar se tem as letras em todas as palavras contidas no array
3.verificar se a próxima letra tem em todas as strings do array
'''