# 현재 경로 ./
# 상위 경로 ../
# 아무것도 없으면 현재경로

import os

# 현재 작업 디렉토리
print(os.getcwd())

# 1.파일 쓰기 (새로 열어 덮어쓴다)
example_file = open('file_example_study.txt', 'w')
example_file.write("파일 생성해보자.")
example_file.close()

# 2. 파일 업데이트 (a)
example_file = open('file_example_study.txt', 'a')
example_file.write("파일 생성 후 수정")
example_file.close()

# 3.파일 읽기
read_file = open('file_example_study.txt', 'r')
data = read_file.read()
read_file.close()
print(data)

# 4. 바이너리로 파일 읽기
read_file = open('file_example_study.txt', 'rb')
data = read_file.read()
read_file.close()
print("바이너리 : ", data)
print("인코딩 : ", data.decode('utf-8'))
