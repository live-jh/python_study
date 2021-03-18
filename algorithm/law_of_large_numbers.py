n, m, k = map(int, input().split())

# n 베열 길이
# m 총 연산 횟수
# k 연속 덧셈 횟수
# print(n, m, k)

data_list = list(map(int, input().split()))
data_list.sort(reverse=True)

print(data_list)
result = 0
tmp = 0
first_no = data_list[0]
second_no = data_list[1]
while True:
    if tmp == m:
        break
    if tmp % k == 0:
        result += second_no
        tmp += 1
    for j in range(k):
        result += first_no
        tmp += 1
        print(tmp)
        print(result)

print(result)
