
import java.util.Arrays;
public class Knapsack {

    public static int knapsack(int[] weights, int[] values, int capacity) {
        int n = values.length;

        int[][] dp = new int[n + 1][capacity + 1];

        for (int i = 1; i <= n; i++) {
            for (int w = 1; w <= capacity; w++) {
                if (weights[i - 1] <= w) {
                    // Барааг нэмж болно
                    dp[i][w] = Math.max(dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
            System.out.println(Arrays.toString(dp[i]));
        }

        return dp[n][capacity];
    }
    public static void main(String[] args) {
        int[] weights = {1, 2, 3, 4};
        int[] values = {10, 20, 30, 40};
        int capacity = 5;

        int maxValue = knapsack(weights, values, capacity);

        System.out.println("Та хамгийн ихдээ нийт: " + maxValue + " төгрөгний барааг даах нь ээ");
    }
}
