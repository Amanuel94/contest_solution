from collections import Counter 

N = int(input())

names = set(input().split())
names = list(names.difference(set(input().split())))

names = list(map(Counter, (map(list, names))))

count = len(names)

for name in names:
    
    val = list(name.values())[0]
    
    for key in name.keys():
        
        if name[key] != val:
            
            count-=1
            break;
print(count)
            
            
    

