#在列表之间移动元素，利用pop()函数
unconfirmed_users = ['qwe','wasd','eghjk','rasd','tkjhg','yerf','uvvf']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print('Verifying user:  ' + current_user.title())

    confirmed_users.append(current_user)

print('\nThe following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())