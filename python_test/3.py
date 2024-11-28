def removeaimval(nums:list[int], val: int) -> int:
    if len(nums) == 0:
        return 0
    else:
        slow = fast = 0
        new = []

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                new.append(nums[fast])
                slow += 1
                fast += 1
            else:
                fast += 1
        print(new)
        return slow
        

list = [1,2,3,4,2,6,7,8]
a = removeaimval(list, 2)
print(a)
