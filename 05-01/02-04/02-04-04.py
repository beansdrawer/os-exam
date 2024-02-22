# 응용 예제! 내 파이썬 프로그램의 이름을 알아보자.
import os
import psutil

for proc in psutil.process_iter():
  
  if proc.pid == os.getpid() :
    print('프로세스명 :', proc.name())