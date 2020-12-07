file = 'pi_digits.txt'
with open(file) as a:
    lines = a.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))