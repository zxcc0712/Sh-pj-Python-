# 斐波那契数列。
# 递归实现
def Fib(n):
    return 1 if n <= 2 else Fib(n - 1) + Fib(n - 2)


print(Fib(int(input())))

# 朴素实现
target = int(input())
res = 0
a, b = 1, 1
for i in range(target - 1):
    a, b = b, a + b
print(a)

