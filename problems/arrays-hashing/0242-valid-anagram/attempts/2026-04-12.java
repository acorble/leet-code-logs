// 242. Valid Anagram（2026-04-12 の解答。Java）
// https://leetcode.com/problems/valid-anagram/

class Solution {
    public boolean isAnagram(String s, String t) {
        // 1文字ずつの配列にしてソートした後Stringに戻して一致判定
        String[] arrs = s.split("");
        String[] arrt = t.split("");

        Arrays.sort(arrs);
        Arrays.sort(arrt);

        String joineds = String.join("", arrs);
        String joinedt = String.join("", arrt);

        if (joineds.equals(joinedt)) {
            return true;
        }

        return false;
    }
}
