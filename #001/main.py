"""
@param: n -> int : Upper Limit of the range
"""
def multiples(n: int) -> int:
    num: list = []
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            num.append(i)
    return sum(num)


if __name__ == '__main__':
    t: int = int(input())
    for _x in range(t):
        n: int = int(input())
        print(multiples(n))
