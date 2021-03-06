empty_tuple = ()
print(type(empty_tuple))

single_tuple = (2,)
print(type(single_tuple))


print('===== 列表元组转换 =====')
my_list = ['wealthy', 'happiness']
print(type(my_list))
my_tuple = tuple(my_list)
print(type(my_tuple))
print(type(list(my_tuple)))


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    tmp = {}
    for i, v in enumerate(nums):
        value = target - v
        if value in tmp:
            return tmp[value], i
        tmp[v] = i
    return ()

# python3
# LeetCode 第1题：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for i, v in enumerate(nums):
            value = target - v
            if value in tmp:
                return tmp[value], i
            tmp[v] = i
        return ()

if __name__ == "__main__":
    print("=" * 50)
    print(twoSum([2, 7, 11, 15], 9))
    # print(twoSum([3, 3], 6))
    # print(Solution().twoSum([2, 7, 11, 15], 9))