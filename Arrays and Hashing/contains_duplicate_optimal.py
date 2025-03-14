def has_duplicates(number_list):
    hashset = set()

    for n in number_list:
        if n in hashset:
            return True
        hashset.add(n)
    return False


my_list = [-1, 2, -3, 2]
print(has_duplicates(my_list))