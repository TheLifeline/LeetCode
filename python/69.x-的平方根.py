#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        heigh=x//2+1
        low=0
        while(True):
            mid=(heigh+low)//2
            if mid == low or mid == heigh:
                break
            temp = mid*mid
            if temp == x:
                return mid
            elif temp<x:
                low=mid
            else:
                heigh=mid
        if heigh*heigh<=x:
            return heigh
        else:
            return low

# if __name__ == "__main__":
#     s = Solution()
#     print(s.mySqrt(8))

        
# @lc code=end

