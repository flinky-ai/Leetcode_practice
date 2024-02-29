nums = [1, 3, 1, 1, 2]

tar = len(set(nums))
N = len(nums)
count = 0

for i in range(0, N - tar + 1):
    print(i, N - tar + 1)
    aux = set(nums[i:i+tar])
    print(aux)
    test = True
    print(test)
    for j in range(tar + i, N):
        print(j, tar + i, N, len(aux))
        if len(aux) < tar:
            aux.add(nums[j])
            print(aux)
        else:
            v = N - j + 1
            count += v
            test = False
            print(count)
            break
    if test and len(aux) >= tar:
            count += 1
print(count)