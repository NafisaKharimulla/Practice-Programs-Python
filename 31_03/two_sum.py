def twoSum(nums, target):
    seen = {}   # value : index

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in seen:
            return [seen[diff], i]

        seen[nums[i]] = i