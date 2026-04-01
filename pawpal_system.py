from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self):
        pass


@dataclass
class Pet:
    name: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets = []

    def add_pet(self, pet: Pet):
        pass

    def get_all_tasks(self):
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_sorted_tasks(self):
        pass

    def filter_tasks(self):
        pass

    def detect_conflicts(self):
        pass