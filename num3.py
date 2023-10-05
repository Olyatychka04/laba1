def members(list):
    proizved = 1
    for i in range(len(list)):
        if i % 2 != 0:
            proizved *= list[i]
    return proizved
list = [1, 2, 3, 4, 5, 8]
result = members(list)
print(result)
def text(list):
    max_value = max(list)
    list.remove(max_value)
    return list
list = [1, 2, 3, 4, 5, 8]
new_list = text(list)
print(new_list)
def large(list):
    list.sort(reverse=True)
    return list[:3]
list = [1, 2, 3, 4, 5]
large_el = large(list)
print(large_el)