with open('input_2_19.txt') as file:
    numbers = []
    file_list = []
    for el in file:
        file_list = file.read().splitlines()
    num_list = [int(j) for i in file_list for j in i.split()]
    count_el = len(num_list)
    print('Size of matrix is {0}x{1}'.format((count_el//2), (count_el//2)))

with open('output_2_19.txt', 'w') as f:
    negative_nums = [el for el in num_list if el < 0]
    for i in range(len(negative_nums)):
        f.write(str(negative_nums[i]))
