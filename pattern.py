N  = int(input())

res = []
for i in range(N):
    
    s = input()
    
    if i == 0:
        
        for j ,c in enumerate(s):
            
            res.append(c)
    
    else:
        
    
        
        for j, c in enumerate(s):
            
            if res and res[j] == c and res[j] != '?':
                
                res[j] = c
                
            elif res and res[j] == c and res[j] == '?':
                
                res[j] = 'x'
                
                
            
            elif res and res[j] != '?' and res[j] != c and  c != '?':
                
                res[j] = '?'
                
            elif res and res[j] != '?' and res[j] != c and  c == '?':
                
                res[j] = res[j]
                
            elif res and res[j] == '?' and res[j] == c:
                
                res[j] = c
                
            elif res and res[j] == '?' and c  == '?':
                
                res[j] = 'x'
     
if N > 1:     
                
    print("".join(res))
else:
        
    for i in range(len(res)):
            
        res[i] = 'x' if res[i] == '?' else res[i]
        
    print("".join(res))
