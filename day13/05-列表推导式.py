arr1 = [x for x in [11, 22, 33, 44, 55]]
print(arr1)

arr2 = [x * 2 for x in [11, 22, 33, 44, 55]]
print(arr2)

arr3 = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(arr3)

arr4 = [x ** 2 for x in range(1, 10)]
print(arr4)

arr5 = [x for x in range(0, 10, 2)]
print(arr5)

arr6 = [x for x in range(1, 10) if x % 2 == 0]
print(arr6)

arr7 = [(x, y) for x in range(1, 10) for y in range(0, 2)]
print(arr7)

arr8 = [(x, y) for x in range(1, 10) for y in range(0, 2) if x % 2 == 0]
print(arr8)
