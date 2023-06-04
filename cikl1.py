#task 1

# sum = 0
# while True:
#     num = int(input("Ввести числo:"))
#     if num == 0:
#         print(sum)
#         break
#     sum +=num
#     print(sum)

#task2

# while True:
#     num = int(input("Ввести число:"))
#     if num ==0:
#         break
#     if num % 3 == 0 and num >=1 and num <=30:
#         print(num)

#task 3

from random import randint
count = 0
random_num = randint(1, 100)
while True:
    num = int(input())

    if num > 1 and  num < 100:
        if num == random_num:
            print("поздравляю, число попыток ", count)
            break
        if num == 0:
            print("exit")
            break
        if num < random_num:
            print("cold")
        elif num > random_num:
            print("hot")
    else:
        print("ВНЕ ДИАПАЗОНА")
    count +=1










