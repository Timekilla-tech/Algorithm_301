import java.util.HashMap;

public class Solution {
    private HashMap<Integer, Integer> cache = new HashMap<>();

    public int fibonacci(int n) {
        if (n <= 1) return n;
        if (cache.containsKey(n)) return cache.get(n);

        int result = fibonacci(n - 1) + fibonacci(n - 2);
        cache.put(n, result);
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 10;
        System.out.println("Fibonacci of " + n + " is " + solution.fibonacci(n));
    }
}
