from multiprocessing import Process
import os
import time

def coke():
    while True :
        print('콜라 프로세스 아이디 :', os.getpid())
        print('나의 부모 프로세스 아이디 :', os.getppid())
        time.sleep(5)

def cider():
    while True :
        print('사이다 프로세스 아이디 :', os.getpid())
        print('나의 부모 프로세스 아이디 :', os.getppid())
        time.sleep(5)

def juice():
    while True :
        print('주스 프로세스 아이디 :', os.getpid())
        print('나의 부모 프로세스 아이디 :', os.getppid())
        time.sleep(5)

if __name__ == '__main__':
  child1 = Process(target=coke, name="Beverage").start()
  time.sleep(0.1)
  child1 = Process(target=cider, name="Beverage").start()
  time.sleep(0.1)
  child1 = Process(target=juice, name="Beverage").start()
  time.sleep(0.1)
  # ps -el | grep "python"