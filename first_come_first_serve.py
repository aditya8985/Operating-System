n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sal = sorted(a, reverse=False)
da = a[0::]
c = [0] * n
for i in range(n):
    c[i] = da.index(sal[i])
    da[da.index(sal[i])] = -1
    print(*c)
final_sum = 0
ltime = min(a)
ct = []
for j in c:
    if ltime<a[j]:
        ltime = a[j] + b[j]
    else:
        ltime = ltime + b[j]
    print("process arriving in", a[j], "seconds finishes in", ltime)
    print(a[j],ltime)
    ct.append(ltime)
print("CT")
print(*ct)
print("Average CT is:", ltime / n)
tat = [0] * n
for i in range(n):
    tat[c[i]] = ct[i] - a[c[i]]
print("TAT")
print(*tat)
print("Average TAT is", sum(tat) / n)
wt = [0] * n
for i in range(n):
    wt[c[i]] = tat[i] - b[c[i]]
print("WT")
print(*wt)
print("Average WT is", sum(wt) / n)