import random

def even(k):
    return k%2 == 0
def odd(k):
    return not even(k)

lst = []
for i in range(10):
    lst.append(random.randint(1,100))
# Find only odd numbers
for i in lst:
    if odd(i):
        print(i)
print("")
# Find only even numbers
for i in range(len(lst)):
    print(f"{i+1}. {lst[i]}")
print("")

N = 1000
d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for i in range(N): # 0 , 1 , 2 , 3 , . . . N
    v = random.randint(1,6)
    d[v] += 1
assert (N == sum(d.values()))
print()
d.clear()
d.pop(4)
d.items()

