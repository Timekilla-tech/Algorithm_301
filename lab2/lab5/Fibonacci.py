def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]
