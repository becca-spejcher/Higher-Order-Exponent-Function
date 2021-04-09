import os
def purpose() :
    """Given a specific directory, the top 10 largest files and the sizes will be printed for that directory."""
def author() :
    """By: Becca Spejcher"""
print(purpose.__doc__)
print(author.__doc__)

while True:
    directory = input('Where should I look?: ')
    if os.path.isdir(directory):
        break
    else:
        print('Please try again.')

lst = []
for (root,dirs,files) in os.walk(directory):
    for f in files:
        lst.append(os.path.join(root,f))

lst.sort(key = os.path.getsize, reverse = True)
for i in range(min(10,len(lst))):
    l = os.path.getsize(lst[i])
    s = str(l/1024) + " KB"
    if True:
        print(f"{i+1}. {lst[i]} : {s}")
    else:
        print("I'm sorry, please try a different file.")





