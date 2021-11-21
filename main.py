import random
with open('words.txt','r', encoding='utf-8') as f:
    words = [line.strip() for line in f]
a1 = words
print('\n\nПрограмма Анаграммы\nПопробуйте отгадать загаданное слово\nЕсли не будет получатся, просто напишите help')
ra1 = len(a1)
rand = random.randint(0,ra1-1)
a2 = a1[rand]
[i.capitalize() for i in a2.split()]
a3 = list(a2)
random.shuffle(a3)
print(a3)
points = 10000
op1 = ''
while op1 != a2:
    op1 = input('Введите ответ: ')
    if op1 == a2:
        print('Поздравляю! Вы угадали слово!')
        break
    elif op1 == 'help':
        points = points / 2
        print(a2[0],' - первая буква в слове')
    else:
        points = points - (points/10)
        print('Неправильно!')
points = int(points)
print('И получили',points,'очков!')
input('Нажмите Enter, чтобы завершить программу ')