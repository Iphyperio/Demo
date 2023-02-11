from random import randint
players = '0'
bot = 2 #2 - бот не играет, 1 - бот играет за Х, 0 бот играет за О

field = [str(i) for i in range(1,10)]
#[0,1,2,3,4,5,6,7,8] #индексы поля
#[1,2,3,4,5,6,7,8,9] #поле

def print_field(field):
    print('*************')
    c = 1
    for i in range(len(field)):
        print('| '+field[i]+' ',end ='')

        if c % 3 == 0:
            print('|',end = '\n')
        c+=1
    print('*************')

def get_data(symbol):
    while True:
        try:
            print(f'Ход игрока "{symbol}"')
            n = int(input('Введите цифру от 1 до 9 '))
            if not(1 <= n <= 9):
                print('Неподходящее значение. Попробуйте еще раз')
            else:
                if field[n-1].isalpha() == True:
                    print('Клетка занята, попробуйте еще раз')
                else:
                    break
        except:
            print('Вы ввели не цифру. Попробуйте еще раз')

    field[n-1] = symbol

def check_win():
    win = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    for variant in win:
        # print('Вариант:',variant)
        if field[variant[0]-1] == field[variant[1]-1] == field[variant[2]-1]:
            if field[variant[0]-1] == 'X':
                print('Победил Крестик!')
                quit()
            else:
                print('Победил Нолик!')

                quit()

    else:
        print('Пока никто не победил')

def player_choise():
    global players,bot

    players = input('Введите количество игроков [1 или 2]: ')
    while players not in ('1','2'):
        players = input('Введите количество игроков [1 или 2]: ')

    if players == '1': #если выбран режим 1 игрок
        player_symbol = input('За кого вы хотите играть X или O? (Введите символ): ')
        while player_symbol not in 'xoXOхоХО0':
            player_symbol = input('За кого вы хотите играть X или O? (Введите символ): ')

        if player_symbol in 'xXхХ':
            bot = 0
            print('Бот ИГРАЕТ ЗА 0!!!!')
        else:
            bot = 1
        print('Игрок ходит за ',player_symbol,'бот играет за',bot)

def bot_turn():
    bot_symbol = 'O' if bot == 0 else 'X'
    while True:
        bot_choise = (randint(1, 10))
        if field[bot_choise - 1].isalpha() == True:
            pass
        else:
            field[bot_choise-1] = bot_symbol
            break




#тут начинается игра
player_choise() #выбор кол-ва игроков
print_field(field) #печать поля в первый раз
turn = 0

while True: #основной цикл
    if players == '2':
        if turn % 2 == 0:
            get_data('X')
        else:
            get_data('O')
    else:
        if bot == 0 and turn % 2 == 1:
            bot_turn()
        elif bot == 1 and turn % 2 == 0:
            bot_turn()
        else:
            if bot == 0:
                get_data('X')
            else:
                print('игрок ходит за 0')
                get_data('O')

    turn += 1
    print_field(field)
    check_win()
