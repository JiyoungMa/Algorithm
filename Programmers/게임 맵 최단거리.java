import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public int solution(int[][] maps) {
        int answer = -1;
        int[][] moves = {{1,0},{-1,0},{0,1},{0,-1}};
        int[][] visited = new int[maps.length][maps[0].length];

        PriorityQueue<int[]> queue = new PriorityQueue(1, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[2] > o2[2]){
                    return 1;
                }else if (o1[2] == o2[2]){
                    return 0;
                }else{
                    return -1;
                }
            }
        });

        visited[0][0] = 1;
        int[] start = {0,0,0};
        queue.add(start);

        while (!queue.isEmpty()){
            int[] now = queue.remove();
            if(now[0] == maps.length && now[1] == maps[0].length){
                break;
            }

            for (int i = 0; i<4; i++){
                int[] next = {now[0]+moves[i][0], now[1]+moves[i][1],now[2]+1};

                if (next[0]<0 || next[0]>=maps.length || next[1]<0 || next[1]>=maps[0].length){
                    continue;
                }

                if (maps[next[0]][next[1]] == 1 && visited[next[0]][next[1]]==0){
                    visited[next[0]][next[1]] = visited[now[0]][now[1]] + 1;
                    queue.add(next);
                }
            }
        }

        if (visited[maps.length-1][maps[0].length-1] != 0){
            answer = visited[maps.length-1][maps[0].length-1];
        }
        return answer;
    }
}
