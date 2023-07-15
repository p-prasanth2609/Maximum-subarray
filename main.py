a, b = map(int, input().split())
c = list(map(int, input().split()))
max_sum = 0
current_sum = 0
j = 0

for i in range(a):
    current_sum += c[i]

    while current_sum > b:
        current_sum -= c[j]
        j += 1

    max_sum = max(max_sum, current_sum)

print(max_sum)
