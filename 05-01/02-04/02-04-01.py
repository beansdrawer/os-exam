from multiprocessing import Process
import os

def func():
    print('안녕, 나는 실험용으로 막 만든 함수야!')
    print('나의 프로세스 아이디 :', os.getpid())
    print('나의 부모 프로세스 아이디 :', os.getppid())

if __name__ == '__main__':
  print('기존 프로세스 아이디 :', os.getpid())
  child = Process(target=func).start()