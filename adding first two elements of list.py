import random
def sum2(nums):
    if len(nums) == 0:
        return 0
    if len(nums)<2:
        return sum(nums)
    else:
        return nums[0] + nums[1]
list= random.sample(range(0,50),5)
print(list)
print(sum2(list))

