# Uses python3
import sys

def optimal_j(W, w):
    res = [[0 for x in range(W + 1)] for y in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            res[i][j] = res[i-1][j]
            if w[i-1] <= j:
                v = w[i-1] + res[i-1][j - w[i-1]]
                if v > res[i][j]:
                    res[i][j] = v

    # return res
    return res[n][W]
    # write your code here
    #result = 0
    #for x in w:
    #    if result + x <= W:
    #        result = result + x
    #return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_j(W, w))
