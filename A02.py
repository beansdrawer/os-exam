import concurrent.futures
import time

def task(name):
    print(f"{name} 시작")
    print(f"{name}가 인사를 하네요. 안녕!!")
    print(f"{name} 종료")
    return f"{name}의 result 값 반환"

if __name__ == "__main__":
    # 최대 3개의 프로세스를 가진 프로세스 풀 생성
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        # 프로세스 풀에 작업 제출
        future_to_name = {executor.submit(task, f"Task-{i}"): f"Task-{i}" for i in range(5)}

        # 작업 완료된 순서대로 결과 출력
        for future in concurrent.futures.as_completed(future_to_name):
            name = future_to_name[future]
            try:
                result = future.result()
                print(f"{name} result: {result}")
            except Exception as e:
                print(f"{name} generated an exception: {e}")
