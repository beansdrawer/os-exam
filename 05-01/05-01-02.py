# 파일없음 예외는 운영체제 예외의 하위 클래스이다 

try : 
  f = open("none.txt", "r")
  print(f.read())
  f.close()
except FileNotFoundError as e:
  print(e)
  print(issubclass(FileNotFoundError, OSError))
