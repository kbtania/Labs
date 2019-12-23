# Дано список імен студентів в межах групи. З’ясувати чи є серед них тезки.

students_count = int(input('General amount of students: '))
students_dic = {i: input('Enter name of student: ') for i in range(students_count)}
name_list = list(students_dic.values())
if len(set(name_list)) == len(name_list):
    print('Everyone has different name')
else:
    print('Some students have the same name')
