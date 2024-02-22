import threading
import os

def func():
    print('안녕, 나는 실험용으로 대충 만든 함수야!')
    print('나의 부모 프로세스 아이디 :', os.getpid()) # 엄밀히 따지면 부모 프로세스란 표현은 맞지 않음
    print('스레드 아이디 :', threading.get_native_id())
    

if __name__ == '__main__':
  print('기존 프로세스 아이디 :', os.getpid())
  thread1 = threading.Thread(target=func).start()