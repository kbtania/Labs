numbers = int(input('Кількість елементів = '))
num_list = [float(input('Чиcло = ')) for x in range(numbers)]
num_list_result = [i for i in num_list if abs(i) > 1]
difference = len(num_list) - len(num_list_result)
for x in range(difference):
    num_list_result.append(0)
print(num_list_result)
