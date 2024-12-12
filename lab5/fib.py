import unittest
def fibonacci(n, cache=None):
    if cache is None:
        cache = {}
    
    if n in cache:
        return cache[n]
    
    if n == 0:
        cache[n] = 0
    elif n == 1:
        cache[n] = 1
    else:
        cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    
    return cache[n]


class TestFibonacci(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_small_numbers(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
    
    def test_large_number(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
    
    def test_cache_efficiency(self):

        cache = {}
        fibonacci(30, cache)
        self.assertEqual(len(cache), 31)

if __name__ == "__main__":
    unittest.main()

