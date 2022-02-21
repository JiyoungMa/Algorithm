import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        PriorityQueue<int[]> queue = new PriorityQueue<>(1, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0]>o2[0]){
                    return 1;
                }else if (o1[0] == o2[0]){
                    return 0;
                }else{
                    return -1;
                }
            }
        });
        int[] visited = new int[n+1];
        Map<Integer, Queue> graph = new HashMap<>();
        for (int i = 1; i<=n;i++){
            Queue<Integer> related = new LinkedList<>();
            graph.put(i, related);
        }

        for (int i = 0; i< edge.length; i++){
            int a = edge[i][0];
            int b = edge[i][1];

            Queue queue1 = graph.get(a);
            queue1.add(b);

            Queue queue2 = graph.get(b);
            queue2.add(a);
        }

        int[] start = {1,1};
        visited[1] = 1;
        int max_visit = 0;
        int count = 0;
        queue.add(start);

        while (!queue.isEmpty()){
            int[] now = queue.remove();
            int now_visitied = now[0];
            int now_location = now[1];

            if (now_visitied == max_visit){
                count++;
            }else if (now_visitied > max_visit){
                max_visit = now_visitied;
                count = 1;
            }

            Object[] now_queue = graph.get(now_location).toArray();

            for (int i = 0; i<now_queue.length; i++){
                int next = (int)now_queue[i];
                if (visited[next] == 0){
                    visited[next] = now_visitied + 1;
                    int[] next_arr = {now_visitied+1, next};
                    queue.add(next_arr);
                }
            }
        }

        answer = count;
        return answer;
    }
}
