class Solution(object):

    def productExceptSelf(self, nums):
        result = []

        for i in range(len(nums)):
            leftProduct = 1 if i == 0 else self.Call(0, i, nums)
            rightProduct = 1 if i == len(nums) - 1 else self.Call(i + 1, len(nums), nums)

            result.append(leftProduct * rightProduct)

        return result

    def Call(self, start, end, nums):
        pro = 1
        for i in range(start, end):
            pro *= nums[i]
        return pro




result = Solution()
print(result.productExceptSelf([-1,1,0,-3,3]))