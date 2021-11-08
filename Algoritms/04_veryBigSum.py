
def aVeryBigSum(ar):
    return sum(ar)


if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    print(result)