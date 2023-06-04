#task 1
# number = int(input("Ввести число от 1 до 100 = "))
# if number < 1 or number > 100:
#     print("число вне диапазона")
#
# elif number % 3 == 0 and number % 5 == 0:
#     print("Fizz Buzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
#
# else:
#     print(number)
#task 2
#Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше 1000 — 8%.
# Пользователь вводит с клавиатуры уровень продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию 200$, вывести итоги на экран.
# Учитывайте следущий факт, что все менеджеры могут иметь
# одинаковый уровень продаж - в таком случае выдайте премию в 200$ всем трём менеджерам.
# manager_1 = int(input("Уровень продаж 1го менеджера = "))
# manager_2 = int(input("Уровень продаж 2го менеджера = "))
# manager_3 = int(input("Уровень продаж 3го менеджера = "))
#
# if manager_1 <= 500:
#     percentage_of_sales = 0.03
# elif manager_1 >= 500 or manager_1 <= 1000:
#     percentage_of_sales = 0.05
# elif manager_1 >= 1000:
#     percentage_of_sales = 0.08
#
# if manager_2 <= 500:
#         percentage_of_sales = 0.03
# elif manager_2 >= 500 or manager_2 <= 1000:
#         percentage_of_sales = 0.05
# elif manager_2 >= 1000:
#         percentage_of_sales = 0.08
#
# if manager_3 <= 500:
#     percentage_of_sales = 0.03
# elif manager_3 >= 500 or manager_3 <= 1000:
#     percentage_of_sales = 0.05
# elif manager_3 >= 1000:
#     percentage_of_sales = 0.08
#
# salary_manager_1 = 200 + manager_1 * percentage_of_sales
# salary_manager_2 = 200 + manager_2 * percentage_of_sales
# salary_manager_3 = 200 + manager_3 * percentage_of_sales
# print("Зарплата 1го менеджера", salary_manager_1)
# print("Зарплата 2го менеджера", salary_manager_2)
# print("Зарплата 3го менеджера", salary_manager_3)
#
# if (salary_manager_1 > salary_manager_2 and salary_manager_1 > salary_manager_3):
#     total = 200 + salary_manager_1
#     print(total, "Лучшим менеджером является 1ый менеджер ")
# elif (salary_manager_2 > salary_manager_1 and salary_manager_2 > salary_manager_3):
#     total = 200 + salary_manager_2
#     print(total,"Лучшим менеджером является 2oй менеджер ")
# elif (salary_manager_3 > salary_manager_1 and salary_manager_3 > salary_manager_2):
#     total = 200 + salary_manager_3
#     print(total,"Лучшим менеджером является 3ий менеджер ")\
#
# if (salary_manager_1 == salary_manager_2 and salary_manager_1 > salary_manager_3 and salary_manager_2 > salary_manager_3):
#     total = 200 + salary_manager_1
#     total = 200 + salary_manager_2
#     print(total, "лучшими менеджерами являются 1ый и 2ой ")
# elif (salary_manager_2 == salary_manager_3 and salary_manager_2 > salary_manager_1 and salary_manager_3 > salary_manager_1):
#   total = 200 + salary_manager_2
#   total = 200 + salary_manager_3
#   print(total, "лучшими менеджерами являются 3ый и 2ой ")
# elif (salary_manager_1 == salary_manager_3 and salary_manager_1 > salary_manager_2 and salary_manager_3 > salary_manager_2):
#   total = 200 + salary_manager_1
#   total = 200 + salary_manager_3
#   print(total, "лучшими менеджерами являются 1ый и 2ой ")
#task 3
#Написать программу подсчета стоимости разговора для разных мобильных операторов. Мобильные операторы: Bakcell, Nar, Azercell.
# Пользователь вводит с какого на какой оператора он звонит и время в секундах.
# Требуется вычислить стоимость разговора в манатах и вывести результат на экран
from_operator = input("ввести оператор,с которого сделан  звонок: ")
to_operator = input("ввести  оператор,на который сделан звонок: ")
duration = int(input("продолжительность разговора в секундах: "))
if from_operator == "bakcell":
    to_operator == "bakcell"
    tarif = 0.03
elif from_operator == "bakcell":
    to_operator == "nar"
    tarif = 0.05
elif from_operator == "bakcell":
    to_operator == "azercell"
    tarif = 0.07

if from_operator == "nar":
    to_operator == "bakcell"
    tarif = 0.05
elif from_operator == "nar":
    to_operator == "nar"
    tarif = 0.03
elif from_operator == "nar":
    to_operator == "azercell"
    tarif = 0.06

if from_operator == "azercell":
    to_operator == "bakcell"
    tarif = 0.07
elif from_operator == "azercell":
    to_operator == "nar"
    tarif = 0.06
elif from_operator == "azercell":
    to_operator == "azercell"
    tarif = 0.03

price = tarif  * duration / 60
print ( "Стоимость звонка" , price)




















