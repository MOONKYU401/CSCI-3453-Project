def find_energy_efficient_cpu(task_util, cpus):
    print(f"Filter CPUs that can run the task")
    candidates = [c for c in cpus if c["capacity"] >= task_util]
    print("  Candidates:", [c["name"] for c in candidates])

    print("Pick the candidate with lowest energy per cycle")
    best = min(candidates, key=lambda c: c["energy_per_cycle"])
    print("  Selected:", best["name"])
    return best

def compute_energy(src, tgt, task_util):
    print("Compute energy if stayed vs migrated")
    cycles = task_util * 100  # pretend cycles ∝ util
    e_src = src["energy_per_cycle"] * cycles
    e_tgt = tgt["energy_per_cycle"] * cycles
    print(f"  Energy on {src['name']}: {e_src}")
    print(f"  Energy on {tgt['name']}: {e_tgt}")
    return e_src, e_tgt

# Hard-coded CPUs: name, capacity, energy_per_cycle
cpus = [
    {"name": "LITTLE0", "capacity": 30, "energy_per_cycle": 1.0},
    {"name": "LITTLE1", "capacity": 30, "energy_per_cycle": 1.0},
    {"name": "big0",    "capacity": 60, "energy_per_cycle": 2.0},
    {"name": "big1",    "capacity": 60, "energy_per_cycle": 2.0},
]


def main():

    task = {
        "name": "VideoDecode",
        "util": 25,
        "current_cpu": cpus[2]  # big0
    }

    print(f"Task '{task['name']}' on {task['current_cpu']['name']}")

    # Find best target core
    target = find_energy_efficient_cpu(task["util"], cpus)

    # Compute and print energy costs
    e_src, e_tgt = compute_energy(task["current_cpu"], target, task["util"])

    # Decide whether to migrate or not
    print("Compare energies and decide")
    if e_tgt < e_src:
        print(f"\tMigrating '{task['name']}' from {task['current_cpu']['name']} to {target['name']}")
    else:
        print(f"\tKeeping '{task['name']}' on {task['current_cpu']['name']}")

if __name__ == "__main__":
    main()
