with open('input_1_19.txt') as file:
    numbers = []
    for el in file:
        numbers.append(int(el))
    min_el = min(numbers)
    count_min = numbers.count(min_el)
    res = len(numbers) - count_min
    print(res)
