/*
 * @lc app=leetcode.cn id=191 lang=c
 *
 * [191] 位1的个数
 */

// @lc code=start
int hammingWeight(uint32_t n) {
    int result =0;
    while(n){
        if(n&1==1){
            result++;
        }
        n = n>>1;
    }
    return result;
}
// @lc code=end

