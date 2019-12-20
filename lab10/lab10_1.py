class Number:
    def __init__(self, number):
        self.number = number

    def enter_num(self):
        self.number = int(input('Enter num: '))
        return self.number

    def print_num(self):
        print(self.number)

    def num_count(self):
        return len(str(self.number))

    def sum_nums(self):
        return sum(map(int, str(self.number)))

    def __str__(self):
        return str(self.number)


num = Number(541)
print('Number is {0}'.format(num.print_num()))
print('Count of digits in {0} is {1}'.format(num, num.num_count()))
print('Sum of number in {0} is {1}'.format(num, num.sum_nums()))
