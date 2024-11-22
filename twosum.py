# https://leetcode.com/problems/two-sum


def twoSum(nums, target):
    for i in range(len(nums)):
       for j in range(len(nums)):
           if (nums[i]+nums[j] == target) and i != j:
               return [i,j] 



if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    print(twoSum(nums,target))