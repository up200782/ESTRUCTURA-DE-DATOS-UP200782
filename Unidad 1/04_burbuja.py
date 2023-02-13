a = [5,2,7,9,3,4,6]
print("Lista original:", a)

for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("Lista ordenada:", a)









