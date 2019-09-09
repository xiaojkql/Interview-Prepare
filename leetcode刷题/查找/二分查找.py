""" 二分查找针对的是有序的数组 """

""" 三种返回方式: 没找到返回-1
每找到返回第一个大于的
没找到返回第一个小于的 """


# 纯粹的查找是否包含一个数值
def bs(nums, val):
    """ 包含end """
    start = 0
    end = len(nums)
    while start < end:
        mid = (start+end)//2
        if nums[mid] < val:
            start = mid+1
        elif nums[mid] > val:
            end = mid
        else:
            return mid
    return -1


# 返回第一个大于或者等于的index
def bs_left(nums, val):
    start = 0
    end = len(nums)
    while start < end:
        mid = (start+end)//2
        if nums[mid] < val:
            start = mid+1  # start 始终在移动
        else:
            # nums[mid]>=val
            end = mid
    return start


# 第一个小于的，保证end始终大于val
def bs_right(nums, val):
    start = 0
    end = len(nums)
    while start < end:
        mid = (start+end) >> 1
        if nums[mid] > val:
            end = mid
        else:
            # nums[mid]<=val
            start = mid+1
    return start-1


nums = [1, 2, 3, 4, 4, 4, 6, 6, 7, 9, 9, 12]
print(bs(nums, 9))
print(bs_left(nums, 8))
print(bs_right(nums, 8))
