import time
import signal # 비동기 이벤트(인터럽트) 핸들러 모듈

def handler(signum, frame):
    print('키보드 인터럽트 감지!')
    print('신호 번호:', signum)
    print('스택 프레임:', frame)
    exit()

# signal.SIGINT : 키보드 인터럽트 상수
signal.signal(signal.SIGINT, handler)

while True:
    print('5초 간격으로 출력중...')
    time.sleep(5)