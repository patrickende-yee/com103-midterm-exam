# com103 midterm exam: task tracker system
tasks = [
    ("Program Logic / Coding ", "6h"),
    ("UI / Output Formatting ", "3h"),
    ("Testing & Debugging    ", "2h"),
    ("Documentation / README ", "2h"),
    ("Presentation Slides    ", "2h")
]

# project info
project_title = input("Enter project title: ")
group_name = input("Enter group name: ")

print("\n==================================")
print(" COM 103 PROJECT -- TASK TYPES")
print("==================================")

# display task types using loop
for i in range(len(tasks)):
    print(f"{i+1}. {tasks[i][0]} [{tasks[i][1]}]")

print("==================================")

assigned_tasks = []
total_points = 0

# accept 4 task assignments
for i in range(4):
    print(f"\n--- TASK {i+1} ---")
    task_num = int(input("Task number (0 to skip): "))
    #Skip
    if task_num == 0:
        continue
    #Continue
    if 1 <= task_num <= 5:
        member = input("Member name: ")
        status = input("Status (done/pending): ").lower()

        # 5. Points system
        if status == "done":
            points = 2
        else:
            points = 1

        total_points += points

        assigned_tasks.append((task_num, member, status, points))

# compute results
num_assigned = len(assigned_tasks)
max_points = num_assigned * 2

if max_points > 0:
    progress = int((total_points / max_points) * 100)
else:
    progress = 0

# project status
if progress >= 75:
    project_status = "PROJECT READY!"
elif progress >= 50:
    project_status = "ON TRACK."
else:
    project_status = "NEEDS MORE WORK!"

# print project board
print("\n========================================")
print(f"{project_title} -- TASK BOARD")
print("========================================")

print(f"Project : {project_title}")
print(f"Group   : {group_name}")
print("----------------------------------------")

# display assigned tasks
for i in range(len(assigned_tasks)):
    t_num, member, status, points = assigned_tasks[i]
    task_name, hours = tasks[t_num - 1]

    print(f"[{i+1}] {task_name} [{hours}]")
    print(f"    Assigned to : {member}")
    print(f"    Status      : {status}")
    print(f"    Points      : {points} / 2\n")

print("----------------------------------------")
print(f"Points Earned : {total_points} / {max_points}")
print(f"Progress      : {progress}%")
print(f"Project Status: {project_status}")
print("========================================")
