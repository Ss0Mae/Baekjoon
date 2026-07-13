import java.util.*;
class Solution {
    public String solution(String s) {
        char[] chars = s.toCharArray();
        
        // 2. 오름차순 정렬
        Arrays.sort(chars);
        
        return new StringBuilder(new String(chars)).reverse().toString();
    }
}