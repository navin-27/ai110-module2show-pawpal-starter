from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner
owner = Owner("Naveen")

# Create pets
dog = Pet("Buddy")
cat = Pet("Kitty")

# Add tasks
dog.add_task(Task("Feed dog", "08:00"))
dog.add_task(Task("Walk dog", "09:00"))
cat.add_task(Task("Feed cat", "08:00"))  # same time (conflict)

# Add pets
owner.add_pet(dog)
owner.add_pet(cat)

# Scheduler
scheduler = Scheduler(owner)

print("\nToday's Schedule:")
for task in scheduler.get_sorted_tasks():
    print(f"{task.time} - {task.description}")

# Check conflicts
conflicts = scheduler.detect_conflicts()

if conflicts:
    print("\n⚠ Conflicts detected:")
    for task1, task2 in conflicts:
        print(f"{task1.time} - {task1.description} conflicts with {task2.description}")