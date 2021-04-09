import random
k = random.randint(5,8) # Final list length
l = [2] # Starting list
for i in range (k-1):
    l.append(random.randint(l[-1],2*l[-1]-1))
m = int(l[k//2]) if k%2 == 1 else float((l[(k-1)//2]+l[k//2])/2)
print(f"List: {' '.join(map(str,l))} - Sum: {sum(l)} - Median: {m} - Average: {sum(l)/k}")
