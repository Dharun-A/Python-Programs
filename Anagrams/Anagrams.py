t = int(input())

for i in range(t):
    c = 0
    a = input()
    b = input()
    for i in set(a):
        c += min(a.count(i),b.count(i))
    print((len(a)+len(b))-(c*2))
    
