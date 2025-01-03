# 2270. Number of Ways to Split Array
def waysToSplitArray(nums):
    n = len(nums)
    prefix_sum = [0] * (n+1)
    count = 0
    for i in range(n):
        prefix_sum[i+1] =prefix_sum[i]+nums[i]

    for i in range(n-1):
        last_digits_sum = prefix_sum[n] - prefix_sum[i+1]
        if prefix_sum[i+1]>=last_digits_sum:
            count+=1
    return count






    

    

if __name__ == '__main__':
    nums = [10,4,-8,7] 
    print(waysToSplitArray(nums))
