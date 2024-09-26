class Solution {
    public String[] solution(String[] names) {
        int size = (names.length + 4) / 5;
        
        String[] name = new String[size];
        int index = 0;
        for(int i = 0; i < names.length; i+=5){
                name[index++] = names[i];
        }
        return name;
    }
}