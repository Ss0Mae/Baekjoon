class Solution {
    public boolean solution(String s) {
        char[] chars = s.toCharArray();
        for (int i =0; i<s.length();i++){
            if ((chars[i] >= 'a' && chars[i] <= 'z') || (chars[i] >= 'A' && chars[i] <= 'Z'))
                return false;
        }
        if (s.length() == 4 || s.length() ==6)
            return true;
        return false;
    }
}