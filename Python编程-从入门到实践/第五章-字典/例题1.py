alien = {'colour':'green','points':5}
print(alien)
alien['x_position'] = 0
print(alien)
#遍历字典
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
for key,value in user_0.items():
    print('\nKey: '+key)
    print('Value: '+value)