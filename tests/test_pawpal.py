from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_complete():
    task = Task("Feed dog", "08:00")
    task.mark_complete()
    assert task.completed == True


def test_add_task():
    pet = Pet("Buddy")
    task = Task("Walk dog", "09:00")
    pet.add_task(task)
    assert len(pet.tasks) == 1


def test_sorting():
    owner = Owner("Test")
    pet = Pet("Buddy")

    pet.add_task(Task("Task1", "09:00"))
    pet.add_task(Task("Task2", "08:00"))

    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    tasks = scheduler.get_sorted_tasks()

    assert tasks[0].time == "08:00"


def test_conflict_detection():
    owner = Owner("Test")
    pet = Pet("Buddy")

    pet.add_task(Task("Task1", "08:00"))
    pet.add_task(Task("Task2", "08:00"))

    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1


def test_recurring_task():
    task = Task("Feed dog", "08:00", frequency="daily")

    new_task = task.mark_complete()

    assert new_task is not None
    assert new_task.description == "Feed dog"