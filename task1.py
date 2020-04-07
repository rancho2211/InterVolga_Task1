a = list(map(int, input().split(",")))
result = 0
for i in range(1, len(a)):
    if a[i - 1] == a[i]:
        result += 1
print(result)

