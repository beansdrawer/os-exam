# 경로 및 파일명 다루기 
import os

def searchFile(dirname, extension):
  filenames = os.listdir(dirname)
  for filename in filenames:
    filepath = os.path.join(dirname, filename)
    if os.path.isdir(filepath):
      searchFile(filepath)
    elif os.path.isfile(filepath):
      name, ext = os.path.splitext(filepath)
      if ext == extension : 
        with open(filepath, "r", encoding="utf-8") as f :
          print(f.read())

searchFile("/Users/hoji/yoonho/오즈코딩스쿨/운영체제/os-exam/05-02", ".txt")