nums = [1, 3, 1, 2, 2]

tar = len(set(nums))
N = len(nums)
count = 0

for i in range(0, N - tar + 1):
    print(i)
    aux = set(nums[i:i+tar])
    print(aux)
    test = True
    print(test)
    for j in range(tar + i, N):
        print(tar + i,N)
        if len(aux) < tar:
            aux.add(nums[j])
        else:
            v = N - j + 1
            count += v
            test = False
            break
    if test and len(aux) >= tar:
            count += 1
print(count)