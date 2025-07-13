'''
https://www.codewars.com/kata/5862f663b4e9d6f12b00003b/train/python

Thinkful - Number Drills: Blue and red marbles
'''

def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    azuis_restadas = blue_start - blue_pulled
    vermelhas_restadas = red_start - red_pulled
    total_restadas = azuis_restadas + vermelhas_restadas
    chance = azuis_restadas / total_restadas
    return chance

print(guess_blue(5, 5, 2, 3))