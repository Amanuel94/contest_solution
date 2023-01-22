N  = int(input())

def order(w):
    
    for i in w:
        
        if ord('1') <= ord(i) <= ord('9'):
            
            return int(i)

for i in range(N):
    w  = input().split()
    
    o = sorted(w, key = order)
    
    k = []
    
    for t in o:
        
        s = ""
        
        for j in t:
            
            if not ord('1') <= ord(j) <= ord('9'):
                
                s+=j
                
        k.append(s)
        
    print(" ".join(k))
                
    
    

    
    

    
