import random
def first_last6(nums):
    if nums[0]==6 or nums[-1] == 6:
        return True
    else:
        return False
list= random.sample(range(0,50),5)
print(first_last6(list))