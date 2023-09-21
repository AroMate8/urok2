num1 = int(input('Ведите первое число от 1 го до 1000  '))
num2 = int(input("Введите второе число от 1 го до 1000  "))
for num1 in range(1, min(s, p) + 1):
    num2 = s - num1
    if num1 * num2 == p:
        print(num1,num2)
    else:
        print('Числа невозможно угадать')