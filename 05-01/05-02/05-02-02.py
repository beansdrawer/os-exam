# os 파일 시스템 관련 함수
import os

filenames = os.listdir("/Users/hoji/yoonho/오즈코딩스쿨/운영체제/os-exam/05-02")
print(filenames)

# 디렉터리 여부
print(os.path.isdir(filenames[0]))
print(os.path.isdir("/Users/hoji/yoonho/오즈코딩스쿨/운영체제/os-exam/05-02"))

# 파일 여부
print(os.path.isfile(filenames[0]))
print(os.path.isfile("/Users/hoji/yoonho/오즈코딩스쿨/운영체제/os-exam/05-02/" + filenames[0]))

# 이름과 확장자 분리
filepath = "/Users/hoji/yoonho/오즈코딩스쿨/운영체제/os-exam/05-02/" + filenames[0]
print(filepath)
name, ext = os.path.splitext(filepath)