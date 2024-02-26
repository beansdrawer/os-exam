# memory check.

import psutil
import os

print("메모리 사용량 조회하기")

# virtual_memory : 시스템 메모리 사용량에 대한 통계를 바이트 단위로 표시된 다음 필드를 포함하는 이름이 지정된 튜플로 반환합니다.
print(psutil.virtual_memory()._asdict())
memory_usage = dict(psutil.virtual_memory()._asdict())
total = memory_usage['total'] #  total physical memory (exclusive swap).
available = memory_usage['available'] # 시스템이 스왑되지 않고 프로세스에 즉시 제공할 수 있는 메모리
percent = memory_usage['percent'] # (total - available) / total * 100
print(f"메모리 총량 : {total}")
print(f"메모리 즉시 제공 가능량 (여분) : {available}")
print(f"메모리 사용률 : {percent}%")

# current process RAM usage
pid = os.getpid()
current_process = psutil.Process(pid)

# current_process.memory_info()[0] : 프로세스가 사용한 물리적 메모리입니다
current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2 ** 20
print(f"메모리 사용량 : {current_process_memory_usage_as_KB:.2f} KB")
