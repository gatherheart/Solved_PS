import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p10942 { 

    final private static int TRUE = 1;
    final private static int FALSE = 0;

    private static void buildDP(int N, int[] word, int[][] dp){
        for (int i = 1; i < N + 1; i++)
            dp[1][i] = TRUE;
        for (int i = 1; i < N; i++)
            if (word[i] == word[i+1])
                dp[2][i] = TRUE;

        for (int i = 3; i < N + 1; i++){
            for (int j = 1; i+j-1 < N + 1; j++){
                if (word[j] == word[i+j-1] && dp[i-2][j+1] == TRUE){
                    dp[i][j] = TRUE;
                }
            }
        }   
    }

    public static void main(String[] args) throws IOException {
        int N = 0, M = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        int[] arr = new int [N+1];
        int [][] dp = new int [N+1][N+1];

        st = new StringTokenizer(br.readLine());
        
        for (int i = 1; i < N + 1; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        buildDP(N, arr, dp);

        M = Integer.parseInt(br.readLine());
        for (int i = 1; i < M + 1; i++){
            st = new StringTokenizer(br.readLine());
            int S = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            sb.append(dp[E-S+1][S]+"\n");
        }
        System.out.print(sb.toString());
    }
}
  