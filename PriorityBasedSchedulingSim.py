# Define the Task class
class Task:
    def init(self, name, priority):
        self.name = name
        self.priority = priority # Lower number = higher priority

    # less than operator for priority comparison
    def lt(self, other): 
        return self.priority < other.priority

# Create a static set of tasks with priorities
tasks = [
    Task("Email Sync", 3),
    Task("Video Playback", 2),
    Task("Incoming Call", 0),
    Task("UI Rendering", 1),
    Task("Background App Update", 4)
]

# import priority queue module
import heapq
# Create a priority queue as a min-heap
task_queue = []
for task in tasks:
    heapq.heappush(task_queue, task)

# Simulate the scheduler picking tasks
print("Task execution order based on static priorities:")
while task_queue:
    next_task = heapq.heappop(task_queue)
    print(f"Executing task: {next_task.name} (Priority {next_task.priority})")