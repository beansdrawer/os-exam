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
