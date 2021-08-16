# list []
# 여러 데이터를 동시 저장 가능한 자료구조, 대괄호 [] 사용하며 0개 이상 원소 저장
# 인덱스로 특정 요소에 접근 가능
# 데이터 변경이 가능한 mutable 한 리스트 (변경 가능)
# 대괄호 안에 : 으로 시작, 끝 인덱스를 설정 가능
# 끝 인덱스는 실제 인덱스보다 1을 크게 더 설정 example -> [0:5] list의 index 0번부터 4번까지
# [:] -> 전체, [0:] -> 0부터 끝까지, [:4] 3번 index까지
# list는 딕셔너리의 key값(해쉬)으로 쓸 수 없지만 tuple은 가능 (딕셔너리의 키값은 불변한 값만 올 수 있기 때문)

# 리스트 초기화
import math

list1 = [1, 2, 3, 'sdf', ['a', 'b', True]]
# print("리스트 인덱싱 출력", list1[:4])  # 맨 마지막을 제외하고 앞까지

# 크기가 n이고, 모든 값이 1인 1차원 리스트 초기화
n = 5
exam_list = [1] * n
# print(exam_list)  # [1,1,1,1,1]

# list와 tuple의 차이 -> immutable(변), mutable(불변), 속도 : list < tuple

# tuple
# 여러 데이터를 동시 저장 가능한 자료구조, 소괄호() 사용하며 0개 이상 원소 저장
# 인덱스로 특정 요소에 접근 가능 -> (for문을 이용해 데이터 추출 가능)
# 데이터 변경이 불가능한 immutable 한 리스트 (# TypeError: 'tuple' object does not support item assignment)

tuple1 = (1, "tuple_study")
tuple2 = (3, 4.22)
tuple3 = tuple1 + tuple2
tuple4 = tuple1 * 5

tt = ('a',) + (1231923,) + tuple1[1:]
# print(tuple1)
# tuple1[0] = 2 에러 변경 불가
# print(tuple3)
# print(tuple4)


# dic {}
# 중괄호를 사용 {}
# 자바의 map과 유사한 자료형으로 key : value 1:1 대응 형태의 자료구조
# 하나의 키값엔 하나의 value만 대응, key값은 변경이 불가하지만, value는 변경이 가능
dic = {'name': 'lion', 'age': 1}  # 초기화 방법 1
dic2 = dict(name='lion', age=1)  # 초기화 방법 2

dic['sex'] = 'male'  # 추가
# print(dic2.get('name'))  # lion
del dic['name']  # age, sex
# print(dic)  #
dic.clear()
# print(dic)  # 빈 dic {}

# print(dic2.get('name'))  # 'lion'
# print('name' in dic2)  # True


# 집합 자료형 set()
# set은 수학에서 이야기하는 집합 개념
# 순서가 없고 모든 데이터는 unique 특징 (중복 허용 x)
# 중괄호 사용하는 표현방식은 dict과 비슷하지만 key가 없고 value만 존재
# 사용시 list로 감싸거나 dict, duple로 변환해서 사용하기
demo_set = set("hello check")  # 중복제거 set()
# ["리턴 데이터" for "리턴 데이터" in obj_set "조건"] 리스트로 반환
new_list_demo_set = [demo for demo in demo_set if demo != " "]  # 공백 데이터, 중복(set)을 제외한 실제 str만 리스트로 리턴
new_list_demo_set.sort()  # 정렬
print(new_list_demo_set)


# 파이썬 반올림
# 소수점 반올림 자리가 .5인경우 앞자리(정수)가 홀수면 올림, 짝수면 내림 파이썬 특징
# 앞 정수에 상관없이 반올림하고 싶다면 3항 연산자를 사용하여 강제하거나 decimal 모듈 사용
def changed_round(num):
    if (float(num) % 1) >= 0.5:
        data = math.ceil(num)  # 0.5보다 크거나 같으면 무적권 올림 최소 0.5 이상 올림
    else:
        data = round(num)
    return data


import decimal

x = decimal.Decimal(9 / 2).quantize(decimal.Decimal('1'),
                                    rounding=decimal.ROUND_HALF_UP)
print('4.5 된다 ! ', x)  # 된다
print('4.5 된다 ! ', changed_round(9 / 2))  # 된다
print('4.5 안된다 ! ', round(9 / 2))  # 우와 신기 4.5 에서 반올림하면 5가 되어야 하는데 안됌
# print(round(7 / 2))  # 우와 신기 3.5에서 반올림해서 4가 됌
# print(round(5 / 2))  # 우와 신기 2.5에서 반올림 하면 3이 되어야 하는데 안됌
# print(round(2.5))  # 예상 -> 3? ㄴㄴ 2나옴
# print(round(3 / 2))  # 우와 신기 1.5에서 반올림해서 2가 됌


# 정규표현식

import re

# sub -> 대신하다
# sub("규칙", 변경할 값, "타겟 문자열")
# \w => 글자 {%i} => 1개, \g<1> 그룹 1개 + " " , 공백 기준으로 split()
# reList = re.sub('(\w{%i})' %i,'\g<1> ', s).split()

# match method
# 문자열에서 패턴 찾기 reList = re.sub('(\w{%i})'%i,'\g<1> ', s).split()(도입부)
# re.match(패턴, 문자열)
# re.match(패턴, 문자열).group()

# search method

# 문자열 전체에서 패턴 찾기(문자 중간)
# re.search(패턴, 문자열)
# re.search(패턴, 문자열).group()

# findall method
# 패턴을 모두 찾아 리스트로 반환
# re.findall(패턴, 문자열)

# name = input_set[0]
    # demo[name] = list(map(int, input_set[1:4]))
