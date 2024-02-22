from multiprocessing import Process, Value, Lock

def counter1(snum, cnum, lock):
    lock.acquire()
    print("number = ",end=""), print(cnum)
    try :
      for i in range(cnum):
          snum.value += 1
    finally :
       lock.release()

def counter2(snum,  cnum, lock):
    lock.acquire()
    print("number = ",end=""), print(cnum)
    try :
      for i in range(cnum):
          snum.value += 1
    finally :
       lock.release()

if __name__ == "__main__":
    
  lock = Lock()
  shared_number = Value('i', 0)

  p1 =Process( target= counter1,  args=(shared_number,50000, lock) )
  p1.start()

  p2 = Process( target= counter2,  args=(shared_number,50000, lock) )
  p2.start()
  
  p1.join()
  p2.join()

  print("finally, number = ",end=""), print(shared_number.value)
