from itertools import permutations
nums = [1,1,1,1,1]
n = len(nums)
res = 0
for i in range(n):
    for j in range(i+1,n):
        x = nums[i]
        y = nums[j]
        if x == y:
            res += 1
        else:
            y = list(str(nums[j]) )
            ll = [(int(''.join(i)),i) for i in (list(permutations(y, len(y))))]
            # print(ll)
            count = 0
            for z,fk in ll:
                if z == x:
                    # print(z)
                    for d,e in zip(fk, y):
                        if d != e:
                            count += 1
                            # print(count)
            if count == 2:
                res += 1
print(res)  