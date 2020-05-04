import random
def max_end3(nums):
    if nums[0]>nums[-1]:
        nums= (nums[0]* 3)
    else:
        nums=(nums[-1]* 3)
    return nums
list3= random.sample(range(0,50),3)
print(max_end3(list3))