import random
a = set()
b = set()
while True:
    if len(a) < 20:
        a.add(random.randint(0, 100))
    if len(b) < 20:
        b.add(random.randint(0, 100))
    if len(a) == 20 and len(b) == 20:
        break
print('объединение множеств:', a | b)
print('разность множеств:', a - b)
print('пересечение множеств:', a & b)