#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

for i in range(1,6):
  print(i, 0)

#или

e = 1

while e <= 5:
    print(e,  '0')
    e = e + 1

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
num = 0

for i in range(10):
    answer = int(input('Введите любую цифру: '))
    if answer == 5:
        num += 1
print('Количество пятёрок равно', num)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1,101):
   sum +=i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
op = 1

for i in range(1,11):
   op *=i
print(op)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

integer_number = 2129

print(integer_number%10,integer_number//10)

while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
vat = input('Введите число')
list(vat)
map(int,list(vat))
sum(map(int, list(vat)))
print(sum(map(int, list(vat))))

'''
Задача 7
Найти произведение цифр числа.
'''
vat = input('Введите число')
map(int,list(vat))
n=1
for i in map(int,list(vat)) :
    n = n * i
print(n)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
n = int(input('Введите число'))
y = 0
max = 0
while n > 0:
    last = n%10
    y = y + 1
    if last > max:
        max = last
    n = n // 10
print('Mаксимальная цифрв в числе ', max )

'''
Задача 10
Найти количество цифр 5 в числе
'''
n = int(input('Введите число'))
y = 0
while n >0:
    last = n % 10
    if last == 5 :
        y = y + 1
    n = n // 10
print('Количество цифр 5 равно ', y)