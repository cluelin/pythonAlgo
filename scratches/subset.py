
total_count = 0;
mylist =[]

def loop(count, subsum):

    global total_count
    count = count-1;

    if count == -1:
        return subsum;

    lastvalue = 1;
    if mylist:
        lastvalue = mylist.pop()
        mylist.append(lastvalue)

    for i in range(lastvalue, 13):
        if mylist.count(i) == 0:
            mylist.append(i)
            subsubsum = subsum;
            subsubsum += i;
            if loop(count, subsubsum) == K:
                total_count = total_count +1;
                mylist.pop()
            else:
                mylist.pop()





T = int(input())

for test_case in range(1, T + 1):
    total_count = 0
    mylist = []
    N, K = map(int, (input().split()))


    loop(N,0)

    print("#{0} {1}".format(test_case, total_count) )