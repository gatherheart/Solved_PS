import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p2169 {

    final static int [][] OFFSET = {{0, 1}, {0, -1}, {1, 0}};
    final static int DEFAULT_CACHE_VAL = -0xFFFFFFF;

    private static boolean isOverflow(int x, int y, int N, int M){
        return x < 0 || y < 0 || x >= N || y >= M;
    }

    private static int traverse(int x, int y, int [][] board, int [][][] dp, boolean [][] visited, int N, int M, int prevDir){

        for (int dir = 0; dir < OFFSET.length; dir++){
            int newX = x + OFFSET[dir][0];
            int newY = y + OFFSET[dir][1];
            
            if (isOverflow(newX, newY, N, M) || visited[newX][newY])
                continue;
            
            if (dp[dir][newX][newY] <= dp[prevDir][x][y] + board[newX][newY]){
                dp[dir][newX][newY] = dp[prevDir][x][y]+board[newX][newY];
                visited[newX][newY] = true;
                traverse(newX, newY, board, dp, visited, N, M, dir);
                visited[newX][newY] = false;
            }
            
        }
    
        return dp[prevDir][x][y];
    }

    public static void main(String [] args) throws IOException {
        int N = 0, M = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        int [][] board = new int [N][M];
        int [][][] dp = new int [3][N][M];
        boolean [][] visited = new boolean [N][M];
        
        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++)
                board[i][j] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < 3; i++){
            for(int j = 0; j < N; j++){
                for (int k = 0; k < M; k++){
                    dp[i][j][k] = DEFAULT_CACHE_VAL;
                }
            }
        }

        visited[0][0] = true;
        dp[0][0][0] = board[0][0];
        dp[1][0][0] = board[0][0];
        dp[2][0][0] = board[0][0];

        traverse(0, 0, board, dp, visited, N, M, 0);

        System.out.println(Math.max(dp[0][N-1][M-1], dp[2][N-1][M-1]));
        
    }
}
