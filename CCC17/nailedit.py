woods = int(input())
pieces = list(map(int,input().split(" ")))

def boardlength(pieces):
    sums = []
    for i in range(woods):
        for j in range(i + 1,woods):
            sums.append(pieces[i] + pieces[j])
    
    nums = {i:sums.count(i) for i in sums if sums.count(i) > 1}
    print(nums[0])
    if len(nums) > 1:
        return sums[0:]
    print(nums)
    return max(nums, key=lambda key: nums[key])

print(boardlength(pieces))
