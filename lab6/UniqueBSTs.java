public class UniqueBSTs {

    public static int numTrees(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 1; 
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i] += dp[j - 1] * dp[i - j];
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        int n = 3;
        System.out.println("Number of unique BSTs " + n + " nodes: " + numTrees(n));
    }
}
