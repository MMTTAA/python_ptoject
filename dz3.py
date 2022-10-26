
import random
from time import sleep

humans = 1000
machines = 1000

i=1

def event1():
    global humans
    global machines
    print("Произошло извержение вулкана, лава достигла близлежащие укрытия людей. Погибло 100 человек.. ")
    humans -= 100
    print(f"{humans}   {machines}")
    print("победа машин")

def event2():
    global humans
    global machines
    print("Неожиданный метеоритный дождь упал на город. Погибло 100 машин..")
    machines -= 100
    print(f"{humans}   {machines}")
    print("победа людей")

def event3():
    global humans
    global machines
    print("Ураган снес поселение людей. Погибло 100 человек..")
    humans -= 100
    print(f"{humans}   {machines}")
    print("победа машин")

def event4():
    global humans
    global machines
    print("Цунами неожиданно накрыло базу машин. Погибло 100 машин..")
    machines -= 100
    print(f"{humans}   {machines}")
    print("победа людей")

def event5():
    global humans
    global machines
    print("Сегодня никто не погиб!")
    print(f"{humans}   {machines}")


# def check_victory():
#     if humans == 0:
#         print('Машины победили!!')
#     elif machines == 0:
#         print('Люди победили!!')
#          

while i==1 :

    dice = random.randint(1,5)
    sleep(random.randint(2, 3))

    # if check_victory():
    #     exit()
    if humans == 0:
        print('Машины победили!!')
        exit()
    elif machines == 0:
        print('Люди победили!!')
        exit()

    elif dice == 1:
        event1()
        
    elif dice == 2:
        event2()
        
    elif dice == 3:
        event3()

    elif dice == 4:
        event4()

    elif dice == 5:
        event5()





