# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

I designed a modular system using four main classes: Owner, Pet, Task, and Scheduler.

The Owner class is responsible for managing multiple pets and providing access to all tasks across those pets. The Pet class represents individual animals and stores a list of tasks associated with each pet. The Task class represents specific activities such as feeding, walking, or medication, including attributes like time, frequency, and completion status.

The Scheduler class acts as the central logic layer that retrieves tasks from the Owner and organizes them. It is responsible for sorting tasks, filtering them, and detecting conflicts.

This design separates responsibilities clearly and follows object-oriented programming principles, making the system easy to understand and extend.

---

**b. Design changes**

After reviewing my initial design with AI assistance, I made a small but important improvement by ensuring that the Scheduler interacts with the Owner class to retrieve tasks instead of directly accessing individual pets.

This change improved encapsulation and made the system more modular. I also decided to use Python dataclasses for the Task and Pet classes to simplify code structure and improve readability.

These adjustments helped make the design cleaner and more maintainable.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler primarily considers time as the main constraint, ensuring that tasks are ordered correctly throughout the day. It also considers task completion status and supports recurring tasks such as daily activities.

Time was prioritized because the main goal of the system is to organize tasks efficiently in a daily schedule. Ensuring correct ordering of tasks is essential for usability.

---

**b. Tradeoffs**

One tradeoff in the scheduler is that it only detects conflicts when tasks have exactly the same time, rather than handling overlapping time durations.

This tradeoff simplifies the implementation while still providing useful conflict detection for most basic scheduling scenarios.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools such as VS Code Copilot and Claude to help brainstorm the system design, generate class structures, and implement algorithms.

AI was especially helpful for writing sorting logic, generating test cases, and debugging errors during development.

---

**b. Judgment and verification**

One instance where I did not fully accept an AI suggestion was when refining the conflict detection logic. I modified the implementation to return pairs of conflicting tasks instead of a simple list.

I verified AI suggestions by running the code, testing outputs, and ensuring the logic matched the intended design.

---

## 4. Testing and Verification

**a. What you tested**

I tested core behaviors including task completion, adding tasks to pets, sorting tasks by time, detecting scheduling conflicts, and handling recurring tasks.

These tests are important because they verify that the system’s main functionality works correctly and ensure reliability in managing pet care schedules.

---

**b. Confidence**

I am confident that my scheduler works correctly for the main use cases, including sorting, filtering, and conflict detection.

If I had more time, I would test edge cases such as invalid time formats, overlapping time ranges, and handling pets with no tasks.

---

## 5. Reflection

**a. What went well**

The modular design of the system worked well, especially separating the Scheduler from the data classes. This made the code easier to manage and extend.

---

**b. What you would improve**

If I had more time, I would improve the scheduling logic to handle overlapping time ranges and add priority-based scheduling.

---

**c. Key takeaway**

One key takeaway from this project is the importance of designing a clear system architecture before implementation and effectively using AI as a collaborative tool while still verifying and refining its output.