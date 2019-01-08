
def fill(rec):
    for i in range(rec[0], rec[2]+1):
        for j in range ( rec[1], rec[3] +1):
            if Matrix[i][j] != rec[4] and Matrix[i][j] !=0:
                Matrix[i][j] += rec[4];
            elif Matrix[i][j] == 0:
                Matrix[i][j] = rec[4];

def calc_result(rec):
    count = 0;
    for i in range (0, 11):
        for j in range(0, 11):
            if Matrix[i][j] == 3:
                count += 1;
    return count;


T = int(input())

for testCase in range(1, T+1):
    Matrix = [[0]*11 for i in range(11)]


    N = int(input())
    for i in range (0, N):
        rec = list(map(int, input().split()))

        fill(rec)


    print("#{0} {1}".format(testCase, calc_result(rec)))

