#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
# 这题竟然不用KMP算法就可以过了，这题一直没过的主要原因是我flag拼错了，令人窒息，
# 不过这题如果不用KMP算法的话时间上有点差，有时间可以改一下。 TODO：KMP

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle==None:
            return 0
        else:
            flag=(-1)
            for i in range(len(haystack)-len(needle)+1):
                flag=i
                for j in range(len(needle)):
                    if haystack[i+j]!=needle[j]:
                        flag=(-1)
                        break
                if flag!=(-1):
                    return flag
            return flag

# @lc code=end

