# 내가 푼 문제
# n, m = map(int, input().split())  # n => row 갯수
#
# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))
#
# result = min(arr[0])
# for i in range(len(arr)):
#     if result < min(arr[i]):
#         result = min(arr[i])
#
# print(result)

# 모범 답안
n, m = map(int, input().split())

result = 0
for _ in range(n):
    data = list(map(int, input().split()))
    min_val = min(data)
    result = max(min_val, result)

print(result)
