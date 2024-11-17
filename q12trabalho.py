fibonacci = [1, 1]
fibonaro = []
a = 1
b = 1
c = a + b
while c <= 100:
    c = a + b
    fibonacci.append(c)
    b = a
    a = c
for i in range (20):
    if i not in fibonacci:
        fibonaro.append(i)
print(fibonacci)
print(fibonaro)