N = int(input())

for i in range(N):
    r_ = list(input().split())
    pos = r_[1]
    clrs = input()
    clrs = clrs*2
    
    max_ = 0
    
    l = r = 0
    while r < len(clrs):
        
        while r < len(clrs)  and  clrs[r] != pos:
            r+=1
        l = r
        
        while r < len(clrs) and clrs[r] != 'g':
            r+=1
        
        max_ = max(max_, r-l)
        r+=1
        
        
    print(max_)
