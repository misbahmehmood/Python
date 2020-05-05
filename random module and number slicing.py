import random
def same_first_last(nums):
    if len(nums) >=1 and nums[0]==nums[-1]:
     return True
    else:
        return False
list= random.sample(range(0,50),5)
print(same_first_last(list))

def rotate_left3(nums):
  return nums[1:] + nums[0]
list2= random.sample(range(0,50),3)
print((list2))

