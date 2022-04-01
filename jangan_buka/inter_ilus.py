# return int atau None
def list_ASCII(list_data):
    list_ascii = []
    for elemen in list_data:
        elemen = str(elemen)
        total = 0
        for char in elemen:
            total += ord(char)
        list_ascii.append(total)

    return list_ascii

def str_to_ASCII(string):
    list_ascii = [ord(char) for char in string]
    return list_ascii

def ASCII_to_str(list_ascii):
    string = ""
    for ascii in list_ascii:
        char = chr(ascii)
        string += char
    return string
    
def interpolation_search(list_data, data):
    list_elemen = list_data.copy()


    list_ascii = list_ASCII(list_elemen)
    insertion_sort(list_ascii)
    print("list_ascii = ", list_ascii)
    list_ascii_data = str_to_ASCII(data)
    print("list_ascii_data =", list_ascii_data)
    data_ascii = sum(list_ascii_data)
    print("data_ascii =", data_ascii)

    index = -1
    low = 0
    high = len(list_ascii)-1

    while list_ascii[low] < data_ascii \
        and list_ascii[high] > data_ascii:

        mid = (data_ascii - list_ascii[low]) // (list_ascii[high] - list_ascii[low]) * (high - low) + low

        if list_ascii[mid] < data_ascii:
            low = mid + 1
        elif list_ascii[mid] > data_ascii:
            high = mid - 1
        else:
            index = mid
            break

    if list_ascii[low] == data_ascii:
        index = low
    elif list_ascii[high] == data_ascii:
        index = high

    if index == -1:
        return None
    else:
        elemen = ASCII_to_str(list_ascii_data)
        print(elemen)
        index = list_data.index(elemen)
        return index

def insertion_sort(list_data):
    list_copy = list_data.copy()
    for i in range(1, len(list_copy)):
 
        key = list_data[i]

        j = i-1
        while j >=0 and key < list_data[j] :
                list_data[j+1] = list_data[j]
                j -= 1
        list_data[j+1] = key

a = ["ms1P", "ms4B", "ms5A", "ms10P", "ms12N"]
ascii_a = list_ASCII(a)

insertion_sort(a)
print(a)

index = interpolation_search(a, "ms12N")
print(index)