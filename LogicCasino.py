from decouple import config
import random

def start():
        print('Добро пожаловать в казино')
        balance = int(config('BALANCE'))
        while True:
                commond = input("1 - выход\n"
                                "2 - играть\n")
                if commond == "1":
                        print('До свидания')
                        break
                elif commond == "2":
                        print(f"ваш баланс {balance}")
                        num = list(range(1, 31))
                        print(num)
                        stavka = int(input('введите сумму ставки'))

                        if stavka > balance:
                                print('у вас не достаточно средств')
                                break

                        user_num = int(input('выберите число'))
                        print(f"ваше число- {user_num}")
                        rang = random.randint(1, 31)
                        print(f'ваш слот- {rang}')

                        if user_num >= 31:
                                print('только числа от 1 до 30')
                                continue
                        elif user_num == rang:
                                print(f'вы выиграли {stavka}$')
                                continue
                        else:
                                print(f'вы проиграли {stavka}$')
                                balance -= stavka
                elif balance <= 0:
                        print('у вас закончились деньги')
                        break
start()





