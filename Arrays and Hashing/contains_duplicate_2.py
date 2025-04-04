def has_duplicates(number_list):
    my_set = set()
    for i in number_list:
        if i in my_set:
            return True
        my_set.add(i)
    return False



my_list = [-1, 2, -3, 2]
print(has_duplicates(my_list))