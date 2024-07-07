T = int(input("Введите число: "))
for i in range(1, T+1):
    if i == 7:
        continue
    elif i == 13:
        continue
    elif i == 21:
        continue
    elif i == 29:
        continue
    elif T >= 35:
        print(i)
    else:
        break