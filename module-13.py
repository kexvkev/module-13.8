ticket = int(input("Количество человек: "))
price = []
for i in range(1, ticket + 1):
    age = int(input(f"Возраст {i} участника? "))
    if age < 18:
        price.append(0)
    elif 18 < age < 25:
        price.append(990)
    else:
        price.append(1390)

if ticket > 3:
    a = int(sum(price) - sum(price)/10)
    print("Сумма вашей покупки равна: ", a)
else:
    a = sum(price)
    print("Сумма вашей покупки равна: ", a)
