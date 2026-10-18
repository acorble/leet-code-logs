// 347. Top K Frequent Elements（2026-05-30 の解答。Java）
// https://leetcode.com/problems/top-k-frequent-elements/

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // initialize hashmap
        Map<Integer, Integer> map = new HashMap<>();

        // iterate through nums and count the frequency of each Integer
        for (int num: nums) {
            // store the frequency in map
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        // get each Entry of the map as Set
        Set<Map.Entry<Integer, Integer>> set = map.entrySet();

        // convert the Set to ArrayList
        List<Map.Entry<Integer, Integer>> list = new ArrayList(set);

        // sort the List by the frequency
        list.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        // return first k key of each Entry in the List
        int[] ret = new int[k];
        for (int i = 0; i < k; i++) {
            ret[i] = list.get(i).getKey();
        }

        return ret;
    }
}
