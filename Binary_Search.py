# Recursion
def bs1(target, nums):
    if not nums:
        return False
    mid = len(nums) // 2
    if nums[mid] == target:
        return True
    elif nums[mid] < target:
        return bs1(target, nums[mid+1:])
    else:
        return bs1(target, nums[:mid])
# iterate
def bs2(target, nums):
    if not nums:
        return False
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            r = mid
        else:
            l = mid + 1
    return False
# test
nums = [1, 2, 3, 5, 6, 9]
for n in nums:
    print(bs2(n, nums))
print(bs2(0, nums))
print(bs2(8, nums))
print(bs2(10, nums))
