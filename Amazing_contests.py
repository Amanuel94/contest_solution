N  = int(input())

arr = list(map(int, input().split()))

max_ = arr[0]
min_ = arr[0]
res = 0
for i in range(1, N):

    if arr[i] > max_:
        
        res+=1
        max_ = arr[i]
        
    elif arr[i] < min_:
        
        res+=1
        min_ = arr[i]
        
print(res)
        
        

                
    
    

    
    

    
