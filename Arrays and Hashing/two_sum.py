def two_sum(nums, target):
    my_dict = {}
    for i in range(len(nums)):
        current_diff = target - nums[i]
        if current_diff in my_dict:
            return [my_dict[current_diff], i]
        my_dict.update({nums[i]: i})

