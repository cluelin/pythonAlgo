

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    rec = list(map(int,input().split()))


    

    N, M = map(int, input().split())
    val_arr = list(map(int,input().split()))


    init = 0;
    minSum = sum(val_arr);
    maxSum = min(val_arr);

    while init + M <= N :
        partialSum = 0;
        for i in range(init, init + M):
            partialSum += val_arr[i]
        if partialSum > maxSum:
            maxSum = partialSum
        if partialSum < minSum:
            minSum = partialSum


        init += 1



    print("#{0} {1}".format(test_case, maxSum - minSum))




