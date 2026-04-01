# 🐾 PawPal+

PawPal+ is a smart pet care management system that helps pet owners organize and track daily activities such as feeding, walking, and medication.

---

## 🚀 Features

- Add pets and tasks
- View daily schedule
- Tasks sorted by time
- Filter tasks by status
- Detect scheduling conflicts
- Support for recurring (daily) tasks

---

## 🧠 Smarter Scheduling

- Tasks are sorted using time-based logic
- Conflicts are detected when tasks share the same time
- Recurring tasks automatically generate new instances
- Filtering allows viewing tasks by completion status

---

## 🧪 Testing PawPal+

Run tests using:

```bash
python -m pytest

## 🧩 System Design (UML)

```mermaid
classDiagram

class Owner {
  +name
  +pets
  +add_pet()
  +get_all_tasks()
}

class Pet {
  +name
  +tasks
  +add_task()
}

class Task {
  +description
  +time
  +frequency
  +completed
  +mark_complete()
}

class Scheduler {
  +owner
  +get_sorted_tasks()
  +filter_tasks()
  +detect_conflicts()
}

Owner --> Pet
Pet --> Task
Scheduler --> Owner

