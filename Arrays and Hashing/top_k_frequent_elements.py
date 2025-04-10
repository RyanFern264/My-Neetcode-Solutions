def top_k_freq(nums, k):
    count_dict = {}
    for i in nums:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    top_nums = []
    for j in range(k):
        curr_max = max(count_dict, key=count_dict.get)
        top_nums.append(curr_max)
        del count_dict[curr_max]
    return top_nums




numbers_ = [4,4,4,3,6,6]
k = 2

result = top_k_freq(numbers_, k)

#value : indexes
#value: occurances



