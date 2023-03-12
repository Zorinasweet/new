import os

vin = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
pole = list(range(10))
pk = [4, 0, 2, 6, 8, 1, 3, 5, 7]

xod = 1

clear = lambda: os.system('clear')
isWin = False

while not isWin:

    a = 0
    for i in range(3):
        for j in range(3):
            print(pole[j + a], end='|')
        print('')
        print('------')
        a += 3

    if xod % 2 == 0:
        player = 'X'
    else:
        player = 'O'

    print(f'Ходят {player} ')
    pl_ch = int(input('выбери поле '))

    if str(pole[pl_ch]) not in 'XO':
        pole[pl_ch] = player
    else:
        print('поле занято')

        continue

    if xod > 4:
        for etche in vin:
            if pole[etche[0]] == pole[etche[1]] == pole[etche[2]]:
                isWin = True
                break

    if xod > 9:
        print('у Вас кончились ходы...Ничья')
        break

    clear()
    xod += 1
print('Конец игры!')