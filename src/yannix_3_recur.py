from typing import List
def recur(nums: List[int], index: int) -> bool:
    if len(nums)-1==index :
        return True
    reach = nums[index] + index
    for i in range(index+1, reach+1):
        if(recur(nums, i)):
            return True
    return False

def canJump(nums: List[int]) -> bool:
    return recur(nums, 0)

    # Test outputs
nums_true= [2,3,1,1,4]
print(canJump(nums_true))

nums_false= [3,2,1,0,4]
print(canJump(nums_false))