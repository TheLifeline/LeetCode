/*
 * @lc app=leetcode.cn id=1 lang=c
 *
 * [1] 两数之和
 */

// @lc code=start


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *ret = (int *)malloc(2*sizeof(int));
    int temp;
    for (int i = 0; i < numsSize-1; i++)
    {
        temp = target - nums[i];
        for (int j = i+1; j < numsSize; j++)
        {
            if (temp == nums[j])
            {
                *ret = i;
                *(ret + 1) = j;
                *returnSize = 2;
                return ret;
            }
        }
    }
    return 0;
}


// @lc code=end

