# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии
def requrs(A, B):
    if B == 0:
        return 1
    elif B == 1:
        return A
    else:
        return A * requrs(A, B - 1)


a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
result = requrs(a, b)
print(result)
