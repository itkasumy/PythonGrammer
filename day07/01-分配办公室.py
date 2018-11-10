import random

teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
rooms = [[], [], []]

for teacher in teachers:
    idx = random.randint(0, 2)
    rooms[idx].append(teacher)

print(rooms)

print("over...")
