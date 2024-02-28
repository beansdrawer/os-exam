'''
이 예제에서 processes는 프로세스의 번호를 나타내는 리스트이고, burst_time은 각 프로세스의 실행 시간을 나타내는 리스트입니다. time_quantum은 각 프로세스에 할당되는 최대 실행 시간을 의미합니다.

이 라운드 로빈 알고리즘 구현은 프로세스의 수, 실행 시간, 및 할당된 시간 단위에 따라서 결과가 달라질 수 있습니다. 프로세스 수, 실행 시간, 및 할당된 시간 단위를 적절하게 변경하여 실험해보세요.
'''

def round_robin(processes, burst_time, time_quantum):
    n = len(processes)
    remaining_time = list(burst_time)
    turnaround_time = [0] * n
    waiting_time = [0] * n

    time = 0
    queue = []

    while True:
        all_processes_completed = True

        for i in range(n):
            if remaining_time[i] > 0:
                all_processes_completed = False

                if remaining_time[i] > time_quantum:
                    time += time_quantum
                    remaining_time[i] -= time_quantum
                    queue.append(i)
                else:
                    time += remaining_time[i]
                    turnaround_time[i] = time
                    remaining_time[i] = 0
                    waiting_time[i] = turnaround_time[i] - burst_time[i]

        if all_processes_completed:
            break

    print("Process\tTurnaround Time\tWaiting Time")
    for i in range(n):
        print(f"P{i + 1}\t\t{turnaround_time[i]}\t\t\t{waiting_time[i]}")


# 예제 사용
processes = [1, 2, 3]
burst_time = [10, 5, 8]
time_quantum = 2

round_robin(processes, burst_time, time_quantum)
