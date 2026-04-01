from pawpal_system import Task, Pet

def test_task_complete():
    task = Task("Feed dog", "08:00")
    task.mark_complete()
    assert task.completed == True


def test_add_task():
    pet = Pet("Buddy")
    task = Task("Walk dog", "09:00")
    pet.add_task(task)
    assert len(pet.tasks) == 1