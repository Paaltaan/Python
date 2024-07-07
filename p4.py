number = int(input('Введите целое положительное число: '))
amount_of_numbers = 0
sum_of_numbers = 0

while number:
    if number % 2 == 0:
        sum_of_numbers += number
        number -= 2
        amount_of_numbers += 1
    else:
        number -= 1
print(f'количество четных цифр: {amount_of_numbers}, сумма чётных цифр: {sum_of_numbers}')