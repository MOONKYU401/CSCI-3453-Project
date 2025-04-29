# Energy-Aware Scheduling in Mobile Operating Systems

## Overview

This project explores Energy-Aware Scheduling (EAS) strategies in mobile operating systems. It compares traditional CPU scheduling algorithms (Round Robin, Priority Scheduling) with Energy-Aware and Reinforcement Learning–inspired techniques. Our goal is to balance performance and energy efficiency, especially in power-constrained mobile environments.

## Features

- **Round Robin Scheduler**: Fair task distribution using fixed time quantum.
- **Priority-Based Scheduler**: Tasks prioritized by urgency but without energy consideration.
- **Energy-Aware Scheduler**: Optimizes for both priority and energy cost using a weighted score.
- **MobiRL Simulation**: Simplified reinforcement learning-inspired model for dynamic CPU/GPU frequency scaling.
- **EAS Algorithm Simulator**: Mimics task migration decisions based on energy profiles and CPU core capacity.
- **Android App Standby Simulation**: Models app hibernation behavior based on inactivity.

## Files and Structure

- `OS.py`: Implements Round Robin, Priority, and Energy-Aware schedulers.
- `PriorityBasedSchedulingSim.py`: Simulates static task priority execution.
- `Simplified MobiRL.py`: Simulates CPU/GPU scaling with performance vs. energy trade-offs.
- `EAS_AlgorithmSim.py`: Simulates CPU selection and migration based on energy efficiency.
- `AndroidAppStandbySim.py`: Demonstrates Android-like app hibernation behavior.
- `scheduling_log.txt`: Logs of task executions and scheduling metrics.
- `energy_scheduler_stats.txt`: Frame-level power and QoS stats from the MobiRL simulation.

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository or download the files.
3. Run schedulers:
    ```bash
    python OS.py
    ```
    This generates logs in `scheduling_log.txt`.

4. Run MobiRL simulation:
    ```bash
    python "Simplified MobiRL.py"
    ```
    Results saved in `energy_scheduler_stats.txt`.

5. Run energy-efficient core assignment:
    ```bash
    python EAS_AlgorithmSim.py
    ```

6. Run standby mode simulation:
    ```bash
    python AndroidAppStandbySim.py
    ```

## Technologies Used

- Python 3
- Simulation logic (no external libraries required)
- Heap/Priority Queue for scheduling
- File I/O for logging

## Research Basis

This project draws from recent academic work such as:
- Orthrus (IEEE, 2024): QoS-aware RL scheduler
- MobiRL (ACM, 2025): Frame-smoothness aware reinforcement learning-based scaling
- Linux CFS & Android UClamp scheduling models

