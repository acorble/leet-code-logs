// 271. Encode and Decode Strings（2026-06-01 ごろの解答。Java。NeetCode で解いた）
// https://neetcode.io/problems/string-encode-and-decode

class Solution {

    public String encode(List<String> strs) {
        String encodedString = "";

        // iterate through strs
        for (String str: strs) {
            // count the number of characters of each string
            int numChar = str.length();
            // add the number to the head of each string
            String numCharAndStr = numChar + str;
            // concatenate each combination
            encodedString = encodedString.concat(numCharAndStr);
        }
            
        // return encoded String
        return encodedString;
    }

    public List<String> decode(String str) {
        // debug
        System.out.println(str);

        List<String> decodedStrs = new ArrayList<>();

        // define variable: the number of counted characters
        int countedChar = 0;

        // iterate until the string length is 0
        while (str.length() - countedChar > 0) {
            // debug
            // System.out.println(countedChar);

            int numChar = (int) str.charAt(countedChar) - '0';

            // debug
            // System.out.println(numChar);

            String substring = "";
            // get substring of numChar characters
            // if numChar is 0, substring is ""
            if (numChar != 0) {
                substring = str.substring(countedChar + 1, countedChar + numChar);
            }

            // debug
            if (countedChar == 0) {
                System.out.println(substring);
            }

            // add substring to List
            decodedStrs.add(substring);
            // update countedChar
            countedChar += 1 + numChar;
        }

        // return decoded Strings
        return decodedStrs;
    }
}
