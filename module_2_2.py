first = int(input('Введите три целых числа: '))
second = int(input())
third = int(input())
if first == second and third == third:
    print(3)
elif first == second or first == third or third == second:
    print(2)
else:
    print(0)