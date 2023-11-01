#Q6
# creating a function for insertion
def insertion_sort(list):
    n = len(list)
    for i in range (1, len(list)):
        k = i
        print('round {0}, start: {1}'.format(i, list))
        while (k>0) and (list[k-1] < list[k]):
            temp = list[k]
            list[k] = list[k-1]
            list[k-1] = temp

            k = k-1
        print('round {0}, end: {1}'.format(i, list))
    return list
insertion_sort(list=[2.3, 4.5, 1.2, 8.9, 2.2, 3.5])

