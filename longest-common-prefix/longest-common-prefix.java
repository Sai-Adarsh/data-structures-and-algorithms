class Solution {
    public String longestCommonPrefix(String[] strs) {
        String res = "";
        Arrays.sort(strs, (a, b)-> a.length() - b.length());
        for(int i = 0; i < strs[0].length(); i++) {
            String temp = strs[0].substring(0, i + 1);
            int count = 0;
            for (int j = 1; j < strs.length; j++) {
                for (int end = 0; end < strs[j].length(); end++) {
                    String curr = strs[j].substring(0, end + 1);
                    //System.out.println(temp + " " + curr);
                    if (temp.equals(curr)) {
                        count++;
                    }
                }
            }
            if (count == strs.length - 1) {
                res = temp;
            }
        }
        return res;
    }
}