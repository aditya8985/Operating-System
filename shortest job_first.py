n = int(input())
b = list(map(int, input().split()))
sal = sorted(b, reverse=False)
da = b[0::]
c = [0] * n
for i in range(n):
    c[i] = da.index(sal[i])
    da[da.index(sal[i])] = -1
final_sum = 0
ltime = 0
ct = [0] * n
for j in range(n):
    ltime = ltime + b[c[j]]
    print("process having burst time", b[c[j]], "seconds finishes in", ltime)
    ct[c[j]]=ltime
print("Average CT is:", sum(ct) / n)
print("CT")
print(*ct)
tat = ct
print("TAT")
print(*tat)
print("Average TAT is", sum(tat) / n)
wt = [0] * n
for i in range(n):
    wt[c[i]] = tat[c[i]] - b[c[i]]
print("WT")
print(*wt)
print("Average WT is", sum(wt) / n)
