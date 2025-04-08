def two_sum(nums, target):
    diffs_dict = {}
    for i in range(len(nums)):
        curr_diff = target - nums[i]
        if curr_diff in diffs_dict:
            return [diffs_dict[curr_diff], i]
        diffs_dict[nums[i]] = i


numbers = [3,4,5,7]
target = 7
solution = two_sum(numbers, target)

print(solution)
