# 고수준 파일 연산 (복사 또는 이동)
import os
import shutil

dirname = "C:\\Users\\DELL\\OneDrive\\바탕 화면\\os-exams\\05-02"

filenames = os.listdir(dirname)

for filename in filenames :
  if "tokyo" in filename :
    origin = os.path.join(dirname, filename)
    # shutil.copy(origin, os.path.join(dirname, "copy.txt"))
    # shutil.move(os.path.join(dirname, "copy.txt"), "C:\\Users\\DELL\\OneDrive\\바탕 화면\\os-exams\\copy.txt")