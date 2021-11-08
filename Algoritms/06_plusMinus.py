# Given an array of integers, calculate the ratios of its elements that are 
# positive, negative, and zero. Print the decimal value of each fraction on 
# a new line with 6 places after the decimal.
# 
# input
#   arr = [-4, 3, -9, 0, 4, 1]
#
# output
#   0.500000
#   0.333333
#   0.166667

def plusMinus(arr):
    data = [1 if int(temp) > 0 else -1 if int(temp) < 0 else 0 for temp in arr ]
    return "{0:.6f}".format(data.count(1)/len(arr)) , "{0:.6f}".format(data.count(-1)/len(arr)) , "{0:.6f}".format(data.count(0)/len(arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print(plusMinus(arr))