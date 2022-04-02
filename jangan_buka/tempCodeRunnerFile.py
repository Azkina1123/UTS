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
