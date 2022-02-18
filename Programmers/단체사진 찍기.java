class Solution {
    public int Permutation(String[] arr, String output, boolean[] visited, int depth, int n, int r, String[] data, int data_n){
        int result = 0;
        if (depth == r){
            boolean answer = true;
            for (int i = 0; i<data_n;i++){
                char target1 = data[i].charAt(0);
                char target2 = data[i].charAt(2);
                char compare = data[i].charAt(3);
                int distance = Character.getNumericValue(data[i].charAt(4));
                int real_distance = Math.abs(output.indexOf(target1) - output.indexOf(target2))-1;

                if (compare == '=' && real_distance == distance){
                }else if (compare == '>' && real_distance > distance){
                }else if (compare == '<' && real_distance < distance){
                }else{
                    answer = false;
                    break;
                }
            }
            if (answer == true){
                result = 1;
            }
        }else{
            for (int i = 0; i<n; i++){
                if(visited[i] != true){
                    visited[i] = true;
                    output += arr[i];
                    result += Permutation(arr,output,visited,depth+1,n,r,data,data_n);
                    visited[i] = false;
                    output = output.substring(0,output.length()-1);
                }
            }
        }
        return result;
    }
    
    public  int solution(int n, String[] data) {
        String[] arr = {"A", "C", "F", "J", "M", "N", "R", "T"};
        String output = "";
        boolean[] visited = {false,false,false,false,false,false,false,false};
        int answer = Permutation(arr,output,visited,0,8,8,data,n);

        return answer;
    }
}
