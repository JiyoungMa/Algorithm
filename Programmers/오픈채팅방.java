import java.util.HashMap;
import java.util.Map;

class Solution {
    public String[] solution(String[] record) {
        String[] answer = {};
        Map<String,String> username = new HashMap<>();
        int count = 0;

        for (int i = record.length-1; i>=0 ;i--){
            String[] now_str = record[i].split(" ");
            if (now_str.length == 3) {
                String command = now_str[0];
                String id = now_str[1];
                String name = now_str[2];

                if (username.get(id) == null){
                    username.put(id,name);
                }

                if (command.equals("Change")){
                    count += 1;
                }
            }else{
                continue;
            }
        }

        answer = new String[record.length-count];

        int change_index = 0;

        for (int i = 0; i<record.length; i++){
            String[] now_str = record[i].split(" ");
            if (now_str.length == 3) {
                String command = now_str[0];
                String id = now_str[1];
                String name = now_str[2];

                switch (command){
                    case "Enter":
                        answer[i-change_index] = username.get(id) +"님이 들어왔습니다.";
                        break;
                    case "Change":
                        change_index += 1;
                        break;
                }
            }else{
                String id = now_str[1];
                answer[i-change_index] = username.get(id) +"님이 나갔습니다.";
            }
        }
        return answer;
    }
}
