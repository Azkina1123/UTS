# return int atau None


def insertion_sort(list_data):
    list_copy = list_data.copy()

    for i in range(1, len(list_copy)):
        
        key = list_data[i]
        print("key = ", key)

        j = i-1
        print("j = ", j)
        while j >= 0 and key < list_data[j] :
            print(list_data[j+1], "|", list_data[j], "\n")
            list_data[j+1] = list_data[j]
            j -= 1
            print("j -- ", j)

        list_data[j+1] = key

a = [12000, 8000, 10000, 40000, 20000]
print(a)
insertion_sort(a)
print(a)
