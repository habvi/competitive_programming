n = int(input())
for _ in range(n):
    s = input()
    t = input()
    ss = sorted(s)
    if t == 'abc':
        if 'a' in ss and 'b' in ss and 'c' in ss:
            bl = ss.index('b')
            br = ss.index('c')
            cl = br
            cr = "".join(ss).rfind('c') + 1
            ss = ss[:bl] + ss[cl:cr] + ss[bl:br] + ss[cr:]
    print("".join(ss))