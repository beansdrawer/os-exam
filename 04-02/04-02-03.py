import tracemalloc

# tracemalloc 시작
tracemalloc.start()

# 메모리 할당을 유발하는 작업 예시
# 바이트로 처리하는 이유 : 이진 데이터로 작업하거나 이진 데이터를 처리하는 파일 또는 네트워크 스트림에서 읽고 쓰기 위해서이다.
data = [b'%d' % _ for _ in range(1, 10000)]
joined_data = b' '.join(data)
# print(joined_data)

# 현재 메모리 사용량 출력
current, peak = tracemalloc.get_traced_memory()
print(f"현재 메모리 사용량: {current / 10**6} MB")
print(f"최대 메모리 사용량: {peak / 10**6} MB")

# 메모리 할당 추적 중지
tracemalloc.stop()

# 메모리 할당 추적 정보 출력
# 메모리 블록의 트레이스를 저장하는 데 사용된 tracemalloc 모듈의 메모리 사용량을 바이트 단위로 가져옵니다.
trace_stats = tracemalloc.get_tracemalloc_memory()
print(f"추적하느라 쓴 메모리 사용량: {trace_stats / 10**6} MB")