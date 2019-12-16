# Дано інформацію про відвідувачів деякого сайту (для кожного відвідувача зберігається
# логін). Підрахувати для кожного клієнта кількість відвідувань.
user_count = int(input('General amount of users: '))
user_dic = {i: input('Enter log of user: ') for i in range(user_count)}
log_list = list(user_dic.values())
i: log_list.count(i) for i in log_list
res = {i: log_list.count(i) for i in log_list}
print(res)
