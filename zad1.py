
def reverse(x):
    indx = len(x) - 1
    its = len(x) // 2
    for i in range(0, its):
        temp = x[indx]
        x[indx] = x[i]
        x[i] = temp
        indx -= 1
    return x

list = []
ItemNm = int(input("How many items?"))
for i in range(0, ItemNm):
    list.append(input("Write data "))
print(reverse(list))

#finished