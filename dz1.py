from msilib import _directories
import random

dict = {0: '○',1: '♤', 2: '♡', 3: '◇', 4: '♧', 5: '☆'}
command=""
print('Добро пожаловать в игру ОДНОРУКИЙ БАНДИТ!!!')
cash = float(input('Положите деньги на счет > '))

while cash>0:
    print(f"На вашем счету {cash} рублей!")
    x,y,z = random.randint(0,5), random.randint(0,5), random.randint(0,5)
    if x == y == z == 0:
        cash == 0
        print(f'{dict[x]} {dict[y]} {dict[z]} \nВас счет равен {cash}.\nВы проиграли!')
    elif x == y == z == 1:
        cash += 10
        print(f'{dict[x]} {dict[y]} {dict[z]}\nВас счет равен {cash}.\nПродолжить игру?')
        command = input(">").strip().lower()
        if command == "да" or command == "yes":
            print("~барабаны крутятся~")
        elif command == "нет" or command == "no":
            print("Игра окончена")
            break
        else:
            print('Вы ввели неправильную команду! Начните игру заново!') 
            break 

    elif x == y == z == 2:
         cash += 20
         print(f'{dict[x]} {dict[y]} {dict[z]}\nВас счет равен {cash}.\nПродолжить игру?')
         command = input(">").strip().lower()
         if command == "да" or command == "yes":
            print("~барабаны крутятся~")
         elif command == "нет" or command == "no":
            print("Игра окончена")
            break
         else:
           print('Вы ввели неправильную команду! Начните игру заново!')
           break

    elif x == y == z == 3:
         cash += 30
         print(f'{dict[x]} {dict[y]} {dict[z]}\nВас счет равен {cash}.\nПродолжить игру?')
         command = input(">").strip().lower()
         if command == "да" or command == "yes":
            print("~барабаны крутятся~")
         elif command == "нет" or command == "no":
            print("Игра окончена")
            break
         else:
            print('Вы ввели неправильную команду! Начните игру заново!')
            break

    elif x == y == z == 4:
         cash += 40
         print(f'{dict[x]} {dict[y]} {dict[z]}\nВас счет равен {cash}.\nПродолжить игру?')
         command = input(">").strip().lower()
         if command == "да" or command == "yes":
            print("~барабаны крутятся~")
         elif command == "нет" or command == "no":
            print("Игра окончена")
            break
         else:
            print('Вы ввели неправильную команду! Начните игру заново!')
            break

    else:
        cash -= 1
        print(f'{dict[x]} {dict[y]} {dict[z]}\nВам не выпала комбинация!\n Ваш счет равен {cash} рублей') 
        print('Продолжить игру?')
        command = input(">").strip().lower()
        if command == "да" or command == "yes":
            print("~барабаны крутятся~")
        elif command == "нет" or command == "no":
            #print(command)
            print("Игра окончена")
        else:
            print('Вы ввели неправильную команду! Начните игру заново')
            break
            
    
