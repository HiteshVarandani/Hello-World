from itertools import permutations

def permute(s):
    l = set()
    for p in permutations(s):
        p = ''.join(p)
        l.add(p)
    return l

t=int(input())
for _ in range(t):
    x = list(map(int,input().split()))
    s = '0'*x[0] +'1'*x[1]
    l = permute(s)
    for p in l:

        a = 0
        b = 0
    
        for k in range(x[0]+x[1]):
            for n in range(k,x[0]+x[1]):
                st = p[k]+p[n]
                if st == '01':
                    a+=1
                if st == '10':
                    b+=1
        if(a==x[2] and b==x[3]):
            print('Yes')
            break
    else:
        print('No')
