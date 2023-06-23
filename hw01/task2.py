# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

while True:
    try:
        num = int(input('enter number: '))
    except ValueError:
        print("enter number!")
    else:
        out = 0
        for i in str(num):
            out += int(i)
        print(f'summ nums = {out}')
        break