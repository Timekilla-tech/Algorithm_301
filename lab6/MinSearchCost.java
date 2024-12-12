


public class MinSearchCost{
    public static int findMinCost(int[] keys, int[] freq) {
        int n = keys.length;
        int[][] dp = new int[n][n];
        int[] freqSum = new int[n + 1];

        for(int i=1; i<=n; i++) freqSum[i] = freqSum[i-1] + freq[i-1];

        for(int len = 1; len <=n; len++) for(int i =0; i<= n - len; i++){
            int j = i + len - 1;
            dp[i][j] = Integer.MAX_VALUE;

            for(int r =i; r<=j; r++){
                int left = (r > i) ? dp[i][r-1] : 0;
                int right = (r < j) ? dp[r+1][j] : 0;
                int cost = left + right + (freqSum[j+1] - freqSum[i]);
                dp[i][j] = Math.min(dp[i][j], cost);
            }
        }
        return dp[0][n-1];
    }
    public static void main(String[] args) {
        int[] keys = {5,6};
        int[] freq = {17, 25};

        System.out.println("Min cost: " + findMinCost(keys, freq));
    }
}