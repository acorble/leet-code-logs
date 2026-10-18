// 36. Valid Sudoku（2026-06-04 の解答。Java）
// https://leetcode.com/problems/valid-sudoku/

class Solution {
    public boolean isValidSudoku(char[][] board) {
        // check if all rows are valid (call isValidArray function)
        for (int i = 0; i < board.length; i++) {
            if (!isValidArray(board[i])) {
                return false;
            };
        }
        
        // check if all columns are valid (call isValidArray function)
        for (int i = 0; i < 9; i++) {
            char[] column = new char[board.length];
            for (int j = 0; j < 9; j++) {
                column[j] = board[j][i];
            }
            if (!isValidArray(column)) {
                return false;
            };
        }

        // check if all 3x3 boxed are valid (call isValidArray function)
        if (!isValidBox(0, 0, board) || !isValidBox(3, 0, board) || !isValidBox(6, 0, board) || !isValidBox(0, 3, board) || !isValidBox(3, 3, board) || !isValidBox(6, 3, board) || !isValidBox(0, 6, board) || !isValidBox(3, 6, board) || !isValidBox(6, 6, board)) {
            return false;
        };

        // return result
        return true;
    }

    // function: check if given array does not contain repetition
    // arguments: char[], ouput: boolean
    public boolean isValidArray(char[] arr) {
        // initialize hashmap
        Map<Character, Integer> map = new HashMap<>();

        // iterate through arr
        for (char element: arr) {
            
            if (element == '.') {
                // if element is empty, do nothing
                continue;
            } else {
                // if element is not empty
                if (!map.containsKey(element)) {
                    // if key:element does not exist in map, put that in map
                    map.put(element, 1);
                } else {
                    // if key:element exists in map, return false
                    return false;
                }
            }
        }
            
        // return if valid
        return true;
    }

    public boolean isValidBox(int rowNumStart, int ColNumStart, char[][] board) {
        List<Character> boxList = new ArrayList<>();
        for (int i = rowNumStart; i < rowNumStart + 3; i++) {
            for (int j = ColNumStart; j < ColNumStart + 3; j++) {
                boxList.add(board[i][j]);
            }
        }

        char[] box = new char[boxList.size()];
        for (int i = 0; i < boxList.size(); i++) {
            box[i] = boxList.get(i);
        }

        return isValidArray(box);
    }
}
