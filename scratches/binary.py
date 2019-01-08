def binary_search(start, end , targer, count):



    count = count+ 1;

    mid = int((end+start)/2)

    if mid == targer:
        return count

    if mid == start:
        if mid +1 == targer:
            return count
        else:
            return -1;

    if mid > targer:
        return binary_search(start, mid, targer, count)
    else:
        return binary_search( mid , end, targer, count)



T = int(input())

for test_case in range ( 1 , T+1):
    P, A, B = map(int, input().split())
    #
    # print(binary_search(1, P, A, 0))
    #
    # print(binary_search(1, P, B, 0))

    if binary_search(1, P, A, 0) == binary_search(1, P, B, 0):
        result = "0"
    elif binary_search(1, P, A, 0) < binary_search(1, P, B, 0) :
        result = "A"
    else :
        result = "B"

    print( "#{0} {1}".format(test_case, result) )





