
testVal = input()

test_list = list(testVal)

maped_list = list(map(lambda x : ord('D') - ord(x) +1, test_list));

print(sum(maped_list))
