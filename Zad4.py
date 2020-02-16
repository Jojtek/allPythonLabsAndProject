
def insertsort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

import random
arr=[]
for i in range (20):
    arr.append(random.randrange(1, 101, 1))

sor = arr.copy()
insertsort(sor)
print("\n unsorted array is:")
for i in range(len(arr)):
    print(str(arr[i]) + ", ", end = '')
print("\n sorted array is:")
for i in range(len(sor)):
    print(str(sor[i]) + ", ", end = '')

#finished