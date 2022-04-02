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
    list_ascii_data = str_to_ASCII(data)
    data_ascii = sum(list_ascii_data)

    index = -1
    low = 0
    high = len(list_ascii)-1

    while list_ascii[low] < data_ascii \
        and list_ascii[high] > data_ascii:

        pos = (data_ascii - list_ascii[low]) // (list_ascii[high] - list_ascii[low]) * (high - low) + low
        print(f"\nlow = {low} | high = {high}\
              \nlist[low]  = {list_ascii[low]}\
              \nlist[high] = {list_ascii[high]}\
              \npos        = {pos}\n")
        if list_ascii[pos] < data_ascii:
            low = pos + 1
        elif list_ascii[pos] > data_ascii:
            high = pos - 1
        else:
            index = pos
            break

    if list_ascii[low] == data_ascii:
        index = low
    elif list_ascii[high] == data_ascii:
        index = high

    if index == -1:
        return None
    else:
        elemen = ASCII_to_str(list_ascii_data)
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

a = ["ms1P", "ms12B", "ms3A", "ms44P", "ms5N"]
print("a = ", a)
b = [str_to_ASCII(str) for str in a]
print("b =", b)
ascii_a = list_ASCII(a)
print("ascii_total = ", ascii_a)
insertion_sort(ascii_a)
print("sort = ", ascii_a)

index = interpolation_search(a, "ms5N")
print(index)

print("\npos = ", (355-353)*(4-1)/(408-353) + 1)

# a = ["227-", "abx", "-=0"]
# index = interpolation_search(a, "22(<")
# print("indexxxx = ", index)

