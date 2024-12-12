import java.util.Arrays;

class Item {
    int value, weight;
    Item(int value, int weight) {
        this.value = value;
        this.weight = weight;
    }
}

class FractionalKnapsack {
    public static double getMaxValue(Item[] items, int capacity) {
        Arrays.sort(items, (a, b) -> Double.compare((double) b.value / b.weight, (double) a.value / a.weight));

        double totalValue = 0.0;

        for (Item item : items) {
            if (capacity >= item.weight) {
                // Барааг бүхлээр нь авна
                totalValue += item.value;
                capacity -= item.weight;
            } else {
                // Барааны бутархай хэсгийг авна
                totalValue += item.value * ((double) capacity / item.weight);
                break; // Дүүрсэн
            }
        }

        return totalValue;
    }

    public static void main(String[] args) {
        Item[] items = {
            new Item(60, 10),
            new Item(100, 20),
            new Item(120, 30)
        };
        int capacity = 50;

        double maxValue = getMaxValue(items, capacity);
        System.out.println("Бидний авч чадах хамгийн их нийт хэмжээ = " + maxValue);
    }
}
