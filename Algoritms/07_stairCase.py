# Staircase detail
#
# This is a staircase of size:
#
# 1   #
# 2  ##
# 3 ###
# 4####
#
# Its base and height are both equal to n. 
# It is drawn using # symbols and spaces. 
# The last line is not preceded by any spaces.
# Write a program that prints a staircase of size n.


def staircase(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j <= n-(int(i)):
                print(' ', end='')
            else:
                print('#', end='')
        print()
               

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
