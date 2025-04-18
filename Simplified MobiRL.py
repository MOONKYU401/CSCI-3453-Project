import random

# Frequency levels in MHz (simplified)
CPU_FREQS = [300, 600, 900, 1200, 1500, 1800]
GPU_FREQS = [300, 500, 700, 900]

# Power usage (mW) and performance multiplier for each freq
cpu_power_map = {300: 100, 600: 150, 900: 220, 1200: 300, 1500: 400, 1800: 500}
gpu_power_map = {300: 80, 500: 140, 700: 210, 900: 300}

# Target frame time for 60 FPS
FRAME_TIME_LIMIT = 16.7

def simulate_frame(cpu_freq, gpu_freq, base_workload):
    # Calculate performance scaling
    cpu_perf = cpu_freq / 1800
    gpu_perf = gpu_freq / 900
    effective_workload = base_workload / (cpu_perf * 0.85 + gpu_perf * 0.15)
    frame_time = effective_workload

    # Calculate power consumption
    power = cpu_power_map[cpu_freq] + gpu_power_map[gpu_freq]

    # Reward system
    if frame_time > FRAME_TIME_LIMIT:
        reward = -5 * (frame_time - FRAME_TIME_LIMIT)
    else:
        reward = 2 - (power / 1000)

    return frame_time, power, reward

def simulate_scheduler():
    log = []
    reward_total = 0
    total_frame_time = 0
    total_power = 0
    dropped_frames = 0
    frame_count = 50

    for frame in range(1, frame_count + 1):
        # Generate random workload
        workload = random.choice([15, 25, 18, 30]) + random.uniform(-2, 2)

        # Frequency selection logic (pseudo-scheduling)
        if workload < 17:
            cpu = 600
            gpu = 300
        elif workload < 22:
            cpu = 900
            gpu = 500
        elif workload < 28:
            cpu = 1200
            gpu = 700
        else:
            cpu = 1500
            gpu = 900

        # Run simulation for this frame
        frame_time, power, reward = simulate_frame(cpu, gpu, workload)

        # Track stats
        total_frame_time += frame_time
        total_power += power
        reward_total += reward
        if frame_time > FRAME_TIME_LIMIT:
            dropped_frames += 1

        log.append(f"Frame {frame:02}: CPU {cpu} MHz, GPU {gpu} MHz | "
                   f"Workload: {workload:.2f} ms -> Frame Time: {frame_time:.2f} ms | "
                   f"Power: {power} mW | Reward: {reward:.2f}")

    # Final statistics
    avg_frame_time = total_frame_time / frame_count
    avg_power = total_power / frame_count

    stats = [
        "\n--- Scheduler Statistics ---",
        f"Total Frames Simulated: {frame_count}",
        f"Average Frame Time: {avg_frame_time:.2f} ms",
        f"Dropped Frames (Frame Time > {FRAME_TIME_LIMIT} ms): {dropped_frames}",
        f"Average Power Consumption: {avg_power:.2f} mW",
        f"Total Reward: {reward_total:.2f}"
    ]

    # Print to console
    print("\n".join(log))
    print("\n".join(stats))

    # Write to file using UTF-8 encoding
    with open("energy_scheduler_stats.txt", "w", encoding="utf-8") as f:
        for line in log + [""] + stats:
            f.write(line + "\n")

    print("\n[✓] Log and statistics saved to 'energy_scheduler_stats.txt'")

# Run the simulation
simulate_scheduler()
