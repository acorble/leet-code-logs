// 49. Group Anagrams（2026-05-02 の解答。Java）
// https://leetcode.com/problems/group-anagrams/

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //strs全部HashMap化する（O(n)）
        //Anagram判定と同じ事すればよく、最初の配列length判定は不要。
        //できたらhashmapじゃなくてint[]でもやってみたい
        List<Map<String, Integer>> maps = new ArrayList<>();

        for (String str: strs) {
            // 格納する用のmap
            Map<String, Integer> map = new HashMap<>();

            // strを1文字ずつsplitしてString配列にする
            String[] str_splited = str.split("");

            // 1文字ずつmapに数をカウントしてmapを作る
            for (String each: str_splited) {
                map.put(each, map.getOrDefault(each, 0) + 1);
            }

            // Listにmapを格納する
            maps.add(map);
        }

        //debug
        // System.out.println("maps size:" + maps.size());
        // System.out.println("maps:" + maps);
        // System.out.println("\n");

        //HashMapの配列にする

        //.equals()がtrueなら同じグループ、同じなら同じ配列に入れる。違うなら作る
        //ここで差が出そう。全部for文で繰り返して判別していってもいいけどn-1回の判定が必要。
        List<List<String>> ans = new ArrayList<>();
        List<List<Integer>> ansIndex = new ArrayList<>();

        for (int i = 0; i < maps.size(); i++) {
            // i番目のmapを格納
            Map<String, Integer> map = maps.get(i);

            // もしまだansが空だったら1個目追加する
            if (ansIndex.size() == 0) {
                // 最初の要素としてi番目の元のStringをListに入れたものを追加
                ansIndex.add(new ArrayList<>(List.of(i)));
            } else {
                boolean isHit = false;

                //格納されているansの中の要素数だけ繰り返す
                for (int j = 0; j < ansIndex.size(); j++) {
                    //mapと、繰り返しList要素の最初の要素のIntegerが示すmaps(i)を比較する
                    //一致ならそのグループ（j番目のList）にmapのindex(i)を入れる
                    if (map.equals(maps.get(ansIndex.get(j).get(0)))) {
                        ansIndex.get(j).add(i);
                        isHit = true;
                        break;
                    }
                }

                //for文全部回ってもbreakされなかったらどれとも一致しなかったということなので要素追加
                if (!isHit) {
                    ansIndex.add(new ArrayList<>(List.of(i)));
                }
            }
            // System.out.println("ansIndex:" + ansIndex + "\n");
        }

        //debug
        // System.out.println("ansIndex size:" + ansIndex.size());
        // System.out.println("ansIndex:" + ansIndex + "\n");

        //List<List<Integer>>ができた。これはindexを示すものなので元のStringを入れる
        for (int i = 0; i < ansIndex.size(); i++) {
            //List<List<>>に格納するためのList
            List<String> strList = new ArrayList<>();

            for (int j = 0; j < ansIndex.get(i).size(); j++) {
                strList.add(strs[ansIndex.get(i).get(j)]);
            }

            ans.add(strList);
        }

        return ans;

        //グループを表す配列をList化して返却して終了
    }
}
