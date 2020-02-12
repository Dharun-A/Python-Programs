N = int(input())

for i in range(N):
    SH, SM, EH, EM = map(int, input().split())
    if SM > EM:
        print((EH-SH)-1, (60-SM)+EM)
    else:
        print(EH-SH, EM-SM)
