from collections import deque
import heapq
import copy

# ----------------- Process Class -----------------

class Process:
    def __init__(self, pid, burst_time, arrival_time, priority=0, energy_cost=1):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.arrival_time = arrival_time
        self.priority = priority
        self.energy_cost = energy_cost
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

    def __lt__(self, other):
        return self.priority < other.priority  # For Priority Queue

    def energy_score(self):
        # Lower score is more favorable
        return 0.6 * self.priority + 0.4 * self.energy_cost

# ----------------- Round Robin -----------------

def round_robin(processes, time_quantum, log):
    time = 0
    queue = deque()
    arrived = []
    processes.sort(key=lambda p: p.arrival_time)
    process_list = copy.deepcopy(processes)
    i = 0

    log.append("\nRound Robin Scheduling (Time Quantum = {})".format(time_quantum))

    while queue or i < len(process_list):
        while i < len(process_list) and process_list[i].arrival_time <= time:
            queue.append(process_list[i])
            i += 1

        if not queue:
            time += 1
            continue

        process = queue.popleft()
        if process.remaining_time > time_quantum:
            log.append(f"{process.pid} runs from {time} to {time + time_quantum}")
            time += time_quantum
            process.remaining_time -= time_quantum
            while i < len(process_list) and process_list[i].arrival_time <= time:
                queue.append(process_list[i])
                i += 1
            queue.append(process)
        else:
            log.append(f"{process.pid} runs from {time} to {time + process.remaining_time} (Completed)")
            time += process.remaining_time
            process.completion_time = time
            process.turnaround_time = time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            arrived.append(process)

    return arrived

# ----------------- Priority Scheduling -----------------

def priority_scheduling(processes, log):
    time = 0
    ready_queue = []
    arrived = []
    processes.sort(key=lambda p: p.arrival_time)
    i = 0

    log.append("\nPriority-Based Scheduling")

    while ready_queue or i < len(processes):
        while i < len(processes) and processes[i].arrival_time <= time:
            heapq.heappush(ready_queue, processes[i])
            i += 1

        if not ready_queue:
            time += 1
            continue

        process = heapq.heappop(ready_queue)
        log.append(f"{process.pid} (Priority {process.priority}) runs from {time} to {time + process.burst_time}")
        time += process.burst_time
        process.completion_time = time
        process.turnaround_time = time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        arrived.append(process)

    return arrived

# ----------------- Energy-Aware Scheduling -----------------

def energy_aware_scheduling(processes, log):
    time = 0
    ready_queue = []
    arrived = []
    processes.sort(key=lambda p: p.arrival_time)
    i = 0

    log.append("\nEnergy-Aware Scheduling (Priority + Energy Cost)")

    while ready_queue or i < len(processes):
        while i < len(processes) and processes[i].arrival_time <= time:
            heapq.heappush(ready_queue, (processes[i].energy_score(), processes[i]))
            i += 1

        if not ready_queue:
            time += 1
            continue

        _, process = heapq.heappop(ready_queue)
        log.append(f"{process.pid} (P:{process.priority}, E:{process.energy_cost}) runs from {time} to {time + process.burst_time}")
        time += process.burst_time
        process.completion_time = time
        process.turnaround_time = time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        arrived.append(process)

    return arrived

# ----------------- Logging Metrics -----------------

def print_metrics(processes, log, title):
    log.append(f"\n{title} Metrics:")
    log.append(f"{'PID':<5} {'Arrival':<8} {'Burst':<6} {'Prio':<6} {'Energy':<7} {'CT':<5} {'TAT':<5} {'WT':<5}")
    for p in processes:
        log.append(f"{p.pid:<5} {p.arrival_time:<8} {p.burst_time:<6} {p.priority:<6} {p.energy_cost:<7} {p.completion_time:<5} {p.turnaround_time:<5} {p.waiting_time:<5}")

def write_log(log, filename="scheduling_log.txt"):
    with open(filename, "w") as f:
        for line in log:
            f.write(line + "\n")
    print(f"\nOutput saved to: {filename}")

# ----------------- Main -----------------

def main():
    processes = [
        Process("P1", burst_time=5, arrival_time=0, priority=2, energy_cost=3),
        Process("P2", burst_time=3, arrival_time=1, priority=1, energy_cost=1),
        Process("P3", burst_time=8, arrival_time=2, priority=3, energy_cost=4),
        Process("P4", burst_time=6, arrival_time=3, priority=0, energy_cost=2)
    ]

    log = []

    rr_results = round_robin(copy.deepcopy(processes), time_quantum=3, log=log)
    print_metrics(rr_results, log, "Round Robin Scheduling")

    prio_results = priority_scheduling(copy.deepcopy(processes), log=log)
    print_metrics(prio_results, log, "Priority-Based Scheduling")

    energy_results = energy_aware_scheduling(copy.deepcopy(processes), log=log)
    print_metrics(energy_results, log, "Energy-Aware Scheduling")

    write_log(log)

if __name__ == "__main__":
    main()
