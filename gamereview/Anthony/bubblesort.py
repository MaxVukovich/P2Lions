#point of sorting is to put things in order
#Bubble Sort
#index [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list = [66,4,7,11,14,16,88,72,99,22]

#Point of j and check for swap, is to run it multiple times until the list is sorted instead of once,
for j in range(0,9):
    check_for_swap = False
    for i in range(0,9):
        if list[i] > list[i + 1]:
            swap = list[i]
            list[i] = list[i +1]
            list[i + 1] = swap
            check_for_swap = True
    if check_for_swap == False:
        break

print(j, list)