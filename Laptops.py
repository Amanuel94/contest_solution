number_of_laptops = int(input())

i = 0
zipped = []
while i < number_of_laptops:
    zipped.append(list(map(int, input().split())))
    i+=1
by_p = sorted(zipped, key = lambda x: x[0])
by_q = sorted(zipped, key = lambda x: x[1])
if by_p == by_q:
    print("Poor Alex")
else:
    print("Happy Alex")
