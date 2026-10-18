// 242. Valid Anagram（2026-04-18 の解答。Java）
// https://leetcode.com/problems/valid-anagram/

class Solution {
    public boolean isAnagram(String s, String t) {
        String[] arr_s = s.split("");
        String[] arr_t = t.split("");

        Map<String, Integer> maps = new HashMap<>();
        Map<String, Integer> mapt = new HashMap<>();
        
        for (String char_s: arr_s) {
            if (!maps.containsKey(char_s)) {
                maps.put(char_s, 1);
            } else {
                maps.put(char_s, maps.get(char_s) + 1);
            }
        }

        for (String char_t: arr_t) {
            if (!mapt.containsKey(char_t)) {
                mapt.put(char_t, 1);
            } else {
                mapt.put(char_t, mapt.get(char_t) + 1);
            }
        }
        
        if (maps.equals(mapt)) {
            return true;
        }
        return false;
    }
}
