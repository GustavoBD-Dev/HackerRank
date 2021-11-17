# You are in charge of the cake for a child's birthday. 
# You have decided the cake will have one candle for each 
# year of their total age. They will only be able to blow 
# out the tallest of the candles. 
# Count how many candles are tallest.
#
# candles = [4,2,3,4] return 2

def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == '__main__':
    # candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print(result)