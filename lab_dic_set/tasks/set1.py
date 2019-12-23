# Дано рядок символів. З’ясувати скільки серед вказаних
# символів є таких, які повторюються

symbols = input('Enter some text: ')
unique_count = len(symbols) - len(set(symbols))
print(unique_count)
