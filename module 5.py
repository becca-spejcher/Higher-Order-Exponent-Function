# shortening code
x = int(input('Please enter an integer'))
print('x is positive') if x>=0 else print('x is negative')

# Replace number with square
numbers = [1,2,3,4,5]
for index in range(len(numbers)):
    numbers[index] = numbers[index]**2
print(numbers)

x = [k ** 2 for k in [1,2,3,4,5]]
print(x)
i = [t ** 2 for t in range(1000) if t % 3 == 0]
print(i)

#Removing from list
l = [1,2,3,4]
x = l.pop(2)
print(l)

w = ['a','b','a','b','c']
for s in range(len(w)):
    if w[s] == 'a':
        v=w.pop(s)
print(w)