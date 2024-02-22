# os 파일 시스템 관련 함수
import os

filenames = os.listdir("C:\\Users\\DELL\\OneDrive\\바탕 화면\\os-exams\\05-02")
print(filenames)

# 디렉터리 여부
print(os.path.isdir(filenames[0]))
print(os.path.isdir("C:\\Users\\DELL\\OneDrive\\바탕 화면\\os-exams\\05-02"))

# 파일 여부
print(os.path.isfile(filenames[0]))
print(os.path.isfile("C:\\Users\\DELL\\OneDrive\\바탕 화면\\os-exams\\05-02\\" + filenames[0]))

# 이름과 확장자 분리
filepath = "C:\\Users\\DELL\\OneDrive\\바탕 화면\\os-exams\\05-02\\" + filenames[0]
print(filepath)
name, ext = os.path.splitext(filepath)