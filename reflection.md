# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- I designed a modular system using four main classes: Owner, Pet, Task, and Scheduler.

The Owner class is responsible for managing multiple pets and providing access to all tasks across those pets. The Pet class represents individual animals and stores a list of tasks associated with each pet. The Task class represents specific activities such as feeding, walking, or medication, including attributes like time, frequency, and completion status.

The Scheduler class acts as the central logic layer that retrieves tasks from the Owner and organizes them. It is responsible for sorting tasks, filtering them, and detecting conflicts.

This design separates responsibilities clearly and follows object-oriented programming principles, making the system easy to understand and extend.

**b. Design changes**

- After reviewing my initial design with AI assistance, I made a small but important improvement by ensuring that the Scheduler interacts with the Owner class to retrieve tasks instead of directly accessing individual pets.

This change improved encapsulation and made the system more modular. I also decided to use Python dataclasses for the Task and Pet classes to simplify code structure and improve readability.

These adjustments helped make the design cleaner and more maintainable.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
