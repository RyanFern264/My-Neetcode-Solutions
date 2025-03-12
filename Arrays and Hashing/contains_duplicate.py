def has_duplicates(number_list):
    for i in range (0, len(number_list)):
        current_value = number_list[i]
        number_list.pop(i)
        if current_value in number_list:
            return True
        number_list.insert(0, current_value)
    return False


my_list = [-1, 2, -3, 2]
print(has_duplicates(my_list))