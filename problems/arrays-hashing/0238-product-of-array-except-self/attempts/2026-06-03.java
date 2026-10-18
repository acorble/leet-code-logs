// 238. Product of Array Except Self（2026-06-03 の解答。Java）
// https://leetcode.com/problems/product-of-array-except-self/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        // initialize answer[]
        int[] answer = new int[nums.length];
        int[] prefixes = new int[nums.length];
        int[] suffixes = new int[nums.length];

        prefixes[0] = 1;
        suffixes[nums.length - 1] = 1;

        // iterate through nums: get prefix[]
        for (int i = 1; i < nums.length; i++) {
            // calculate the prefix
            int prefix = prefixes[i-1] * nums[i-1];

            // store the product of the prefix and the suffix in answer[i]
            prefixes[i] = prefix;
        }

        // iterate through nums: get suffix[] and calculate the product
        for (int i = nums.length - 2; i >= 0; i--) {
            // calculate the suffix
            int suffix = suffixes[i+1] * nums[i+1];
            
            suffixes[i] = suffix;

            // store the product of the prefix and the suffix in answer[i]
            answer[i] = prefixes[i] * suffix;
        }
        answer[nums.length - 1] = prefixes[nums.length - 1];
            
        // return answer[]
        return answer;
    }
}
