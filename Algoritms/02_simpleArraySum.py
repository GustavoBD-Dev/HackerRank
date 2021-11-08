# Given an array of integer, find the sum of its elements.

def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    print(result)