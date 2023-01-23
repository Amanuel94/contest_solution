T = int(input())

for i in range(T):
    
    nums = list(map(int, input().split()))
    nums.sort()
    
    print(nums[1])
    
