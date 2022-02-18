class Solution {
    public int solution(String s) {
        int answer = s.length();
        for (int i = 1; i<=s.length(); i++){
            String result = "";
            String prev = "";
            int count = 0;
            for (int start = 0; start < s.length(); start += i){
                if (start+i <= s.length()) {
                    String now = s.substring(start, start + i);
                    if (prev.equals(now)) {
                        count += 1;
                    } else {
                        if (count > 1) {
                            result += Integer.toString(count) + prev;
                        }else{
                            result += prev;
                        }
                        prev = now;
                        count = 1;
                    }
                }else{
                    if (count > 1) {
                        result += Integer.toString(count) + prev;
                    }else{
                        result += prev;
                    }
                    result += s.substring(start,s.length());
                    count = 0;
                    prev = "";
                }
            }
            if (count != 0){
                if (count > 1) {
                    result += Integer.toString(count) + prev;
                }else{
                    result += prev;
                }
            }
            if (answer > result.length()){
                answer = result.length();
            }
        }
        return answer;
    }
}
