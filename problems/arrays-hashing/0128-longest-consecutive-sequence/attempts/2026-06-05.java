// 128. Longest Consecutive Sequence（2026-06-05 の解答。Java）
// https://leetcode.com/problems/longest-consecutive-sequence/

class Solution {
    public int longestConsecutive(int[] nums) {
        // initialize hashset
        Set<Integer> set = new HashSet<>();
        // initialize max length
        int maxLength = 0;

        // store array elements in set
        for (int num: nums) {
            set.add(num);
        }

        // while loop
        while (set.size() > 0) {
            // find the minimum number in set
            int min = Collections.min(set);

            // remove minimum number from set
            set.remove(min);
            
            // initialize count
            int lengthCount = 1;

            // initialize next target
            int nextTarget = min + 1;

            // while loop
            while (true) {
                // check if the next number exists
                if (set.contains(nextTarget)) {
                    // if it exists,
                    // increment the length number
                    lengthCount++;
                    // remove that from set
                    set.remove(nextTarget);

                    //update next target
                    nextTarget++;
                } else {
                    // if it does not exist, 
                    // compare the length number to the max length so far, and update max length
                    if (lengthCount > maxLength) {
                        maxLength = lengthCount;
                    }
                    // break out of the loop
                    break;
                }
            }

        }

        // return max length
        return maxLength;
    }
}
