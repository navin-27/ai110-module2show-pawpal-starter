from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self):
        self.completed = True


@dataclass
class Pet:
    name: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def get_all_tasks(self):
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_sorted_tasks(self):
        return sorted(self.owner.get_all_tasks(), key=lambda t: t.time)

    def filter_tasks(self, completed=None):
        tasks = self.owner.get_all_tasks()
        if completed is None:
            return tasks
        return [t for t in tasks if t.completed == completed]

    def detect_conflicts(self):
        tasks = self.owner.get_all_tasks()
        seen = {}
        conflicts = []

        for task in tasks:
            if task.time in seen:
                conflicts.append(task)
            else:
                seen[task.time] = task

        return conflicts