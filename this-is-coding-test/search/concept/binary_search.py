# 이진 탐색
# 내부 데이터가 정렬되어 있을때 사용할 수 있는 탐색
# 반으로 쪼개서 중간점의 위치에 데이터와 반복적 비교
# 시간복잡도 O(logN) 절반씩 줄어듬 연산횟수는 log2N과 비례
# 반복문을 사용할수도 있고 재귀를 사용할 수도 있음
# 탐색범위가 2,000만이 넘어갈 시 이진 탐색

# 이진탐색트리
# 트리 자료구조중 가장 간단한 형태
# 왼쪽 자식노드는 부모보다 작으며 오른쪽 자식 노드는 부모보다 크다 (왼쪽 자식노드 < 부모노드 < 오른쪽 자식노드)
# 찾고자 하는 숫자를  기준점(부모노드)과 비교해서 찾는 값이 더 크면 오른쪽 노드 반대면 왼쪽 (계속 한쪽 제거해나가기)
# 데이터의 범위가 1,000만개 이상 또는 1,000억개 이상일때 사용하기 좋음

# import sys
# input_data = sys.stdin.readline().rstrip()  # 엔터가 줄바꿈 기호로 입력되어서 이 부분을 제거해줘야함 rstrip()



# 재귀를 활용한 이진 탐색
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2  # 중간 값 구하기
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        end = mid - 1
        return binary_search(array, target, start, end)
    else:
        start = mid + 1
        return binary_search(array, target, start, end)


n, target = map(int, input().split())  # 10 7
array = list(map(int, input().split()))  # 1 3 5 7 9 11 13 15 17 19
if n != len(array):
    print("입력한 n의 길이와 실제 배열의 길이가 같지 않습니다. 다시 실행해주세요.")
else:
    result = binary_search(array, target, 0, n - 1)
    if result is None:
        print("찾는 값이 존재하지 않습니다.")
    else:
        print(result)


# 반복문을 활용한 이진탐색

def for_binary_search(array, target, start, end):
    while start <= end:  # start와 end가 같거나 클때까지 (끝까지)
        mid = (start + end) // 2  # 중간 값 구하기
        if array[mid] == target:
            return mid
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for_n, for_target = map(int, input().split())  # 10 7
for_array = list(map(int, input().split()))  # 1 3 5 7 9 11 13 15 17 19
if for_n != len(for_array):
    print("입력한 n의 길이와 실제 배열의 길이가 같지 않습니다. 다시 실행해주세요.")
else:
    result = for_binary_search(for_array, for_target, 0, for_n - 1)
    if result is None:
        print("찾는 값이 존재하지 않습니다.")
    else:
        print(result)
