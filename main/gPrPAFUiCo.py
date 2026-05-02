def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors

def fibonacci(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_palindrome(s):
    return s == s[::-1]

def sort_numbers(numbers):
    return sorted(numbers)

def count_occurrences(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main():
    print(gcd(48, 18))
    print(lcm(4, 6))
    print(is_prime(29))
    print(prime_factors(28))
    print(fibonacci(10))
    print(factorial(5))
    print(is_palindrome('radar'))
    print(sort_numbers([5, 3, 8, 1]))
    print(count_occurrences(['apple', 'banana', 'apple']))
    print(merge_dicts({'a': 1}, {'b': 2}))
    write_file('test.txt', 'Hello, World!')
    print(read_file('test.txt'))
main()
