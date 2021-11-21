import random
with open('words.txt','r', encoding='utf-8') as f:
    words = [line.strip() for line in f]
a1 = words
points2 = 0
print('\n\nПрограмма Анаграммы\nПопробуйте отгадать загаданное слово\nЕсли не будет получатся, просто напишите help')
print('Вы можете завершить программу с помощью команды stop')
ra1 = len(a1)
op1 = ''
points = 10000
while op1 != 'stop':
    rand = random.randint(0, ra1 - 1)
    a2 = a1[rand]
    [i.capitalize() for i in a2.split()]
    a3 = list(a2)
    random.shuffle(a3)
    print(a3)
    while op1 != a2:
        op1 = input('Введите ответ: ')
        if op1 == a2:
            print('Поздравляю! Вы угадали слово!')
            break
        elif op1 == 'help':
            points = points / 2
            print(a2[0], ' - первая буква в слове')
        elif op1 == 'stop':
            points = points - 10000
            break
        else:
            print('Неправильно!')
            points = points - (points/10)
    points2 = points2 + points
    points2 = int(points2)
    print('И получили', points2, 'очков!')
input('Нажмите Enter, чтобы завершить программу ')