def fibonacci_numbers(ul: int) -> int:
    numbers: list = []
    a: int = 0
    b: int = 1
    total: int = 0
    while (total <= ul):
        numbers.append(total)
        a = b
        b = total
        total = a + b
    return sum(filter(lambda x: not x % 2, numbers))


if __name__ == '__main__':
    t: int = int(input().strip())
    for _x in range(t):
        n: int = int(input().strip())
        print(fibonacci_numbers(n))