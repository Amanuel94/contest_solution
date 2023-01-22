nums=list(map(int,input().split()))
dur=nums[0]
min=nums[1]
thm=list(map(int, input().split()))
pat=list(map(int,input().split()))

ptr = L = out = res=0
t=min


for i in range(dur):
    if pat[i] != 0:
        res +=thm[i]

while ptr < dur:
    if pat[ptr] == 0 and min > 0:
        res += thm[ptr]
        ptr +=1
        out=max(out,res)
        min -=1

    elif pat[ptr] == 1 and min > 0:
        out=max(res,out)
        ptr +=1
        min -=1

    if min == 0:
        if pat[L] == 0:
            res -=thm[L]

        L += 1
        min +=1

print(out)
