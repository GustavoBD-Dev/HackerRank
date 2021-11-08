# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.

def compareTriplets(a,b):
    x,y = 0,0
    for i in range(len(a)):
        if a[i] > b[i]:
            x+=1
            continue
        elif a[i] < b[i]:
            y+=1
            continue
        else:
            continue
    return x , y

        
        

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a,b)
    print(result)
