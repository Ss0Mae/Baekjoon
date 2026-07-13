class Solution {
    public String solution(String s) {
        String answer = "";
        String[] strArr = s.split("");
        int idx = 0;
        
        for (int i = 0; i < strArr.length; i++) {
            if (strArr[i].equals(" ")) {
                idx = 1;
            }
            
            answer += idx % 2 == 0 ? strArr[i].toUpperCase() : strArr[i].toLowerCase();
            idx++;
        }
        
        return answer;
    }
}