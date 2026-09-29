# 🎯 Java Interview Preparation Kit

Comprehensive study guide, high-yield Q&A, and interactive mock interview tool for Java developer assessments (including Internshala AI Assessment, campus placements, and technical rounds).

---

## 📌 Repository Contents

| File | Description |
|---|---|
| [`README.md`](file:///e:/gharkam/interview/README.md) | Core concepts, Top interview questions & answers |
| [`Java_Revision_Marathi.md`](file:///e:/gharkam/interview/Java_Revision_Marathi.md) | सोप्या मराठी भाषेत Quick Revision नोट्स आणि कीवर्ड्स |
| [`mock_interview.py`](file:///e:/gharkam/interview/mock_interview.py) | Interactive Python terminal tool for mock interview practice |

---

## 🚀 Top 10 High-Yield Java Interview Questions & Answers

### 1. What are the four core principles of OOP?
* **Encapsulation:** Wrapping data (variables) and code (methods) together into a single unit (class) and restricting direct access using `private` access specifiers with getters/setters.
* **Inheritance:** Mechanism where one class acquires the properties and behaviors of a parent class (`extends` keyword), promoting code reusability.
* **Polymorphism:** Ability of an object to take many forms.
  * *Compile-time (Method Overloading):* Same method name with different parameter signatures.
  * *Runtime (Method Overriding):* Child class providing a specific implementation of a method defined in its parent class (`@Override`).
* **Abstraction:** Hiding complex implementation details and showing only essential features to the user (achieved via Abstract Classes and Interfaces).

---

### 2. Difference between `==` and `.equals()` method?
* `==` is an **operator** used for **reference comparison** (checks if both references point to the exact same memory location).
* `.equals()` is a **method** in the `Object` class used for **value / content comparison** (checks if the contents of the objects are logically equal).

```java
String s1 = new String("Java");
String s2 = new String("Java");

System.out.println(s1 == s2);      // false (different memory addresses in heap)
System.out.println(s1.equals(s2));  // true (same text content)
```

---

### 3. Difference between String, StringBuilder, and StringBuffer?
* **String:** Immutable (cannot be changed once created). Any modification creates a new object in the String Constant Pool.
* **StringBuilder:** Mutable (can be modified in place), fast, but **not thread-safe** (non-synchronized). Ideal for single-threaded tasks.
* **StringBuffer:** Mutable, **thread-safe** (synchronized methods), but slightly slower than `StringBuilder`.

---

### 4. What is the difference between Interface and Abstract Class?
| Feature | Interface | Abstract Class |
|---|---|---|
| Methods | Abstract methods by default (can have `default` & `static` from Java 8+) | Can have both abstract and concrete methods |
| Multiple Inheritance | Supported (`implements A, B`) | Not supported for classes (`extends A` only) |
| Variables | `public static final` (constants only) | Can have instance variables of any access level |
| Keyword | `interface` / `implements` | `abstract class` / `extends` |

---

### 5. Java Collections: Difference between List, Set, and Map?
* **List:** Ordered collection, allows duplicate values, elements accessed by index. (Examples: `ArrayList`, `LinkedList`).
* **Set:** Unordered collection (unless sorted like `TreeSet`), **does not allow duplicates**. (Examples: `HashSet`, `LinkedHashSet`).
* **Map:** Stores data in **Key-Value pairs**. Keys must be unique, values can be duplicated. (Examples: `HashMap`, `TreeMap`).

---

### 6. How does `HashMap` work internally in Java?
* `HashMap` is based on **Hashing**.
* It uses an array of Nodes/Buckets (`Node<K,V>[] table`).
* When `put(key, value)` is called:
  1. Computes hash code using `key.hashCode()`.
  2. Finds bucket index using `index = hash & (n - 1)`.
  3. If collision occurs, stores entries in a LinkedList.
  4. In Java 8+, if bucket size exceeds 8, LinkedList is converted to a **Red-Black Tree** to improve lookup time from $O(n)$ to $O(\log n)$.

---

### 7. What is the difference between `final`, `finally`, and `finalize`?
* **`final` (keyword):**
  * Final variable $\rightarrow$ Constant (cannot be reassigned).
  * Final method $\rightarrow$ Cannot be overridden.
  * Final class $\rightarrow$ Cannot be inherited.
* **`finally` (block):** Used with `try-catch` blocks. Always executes regardless of whether an exception is thrown or caught (used for resource cleanup).
* **`finalize()` (method):** Called by the Garbage Collector before an object is destroyed (deprecated in modern Java).

---

### 8. Explain Exception Hierarchy in Java (Checked vs Unchecked).
* **Throwable** is the root class (`Exception` and `Error`).
* **Checked Exceptions:** Checked at compile-time. Must be handled with `try-catch` or declared with `throws`. (Examples: `IOException`, `SQLException`).
* **Unchecked Exceptions (`RuntimeException`):** Occur at runtime due to programming flaws. (Examples: `NullPointerException`, `ArithmeticException`, `ArrayIndexOutOfBoundsException`).

---

### 9. What are new features introduced in Java 8?
* **Lambda Expressions:** Anonymous functions (`(a, b) -> a + b`).
* **Functional Interfaces:** Interfaces with exactly one abstract method (annotated with `@FunctionalInterface`, e.g., `Predicate`, `Consumer`, `Function`).
* **Stream API:** Functional-style operations on collections (`filter`, `map`, `reduce`).
* **Default & Static Methods** in Interfaces.
* **Optional Class:** Helps avoid `NullPointerException`.
* **New Date & Time API** (`java.time` package).

---

### 10. What is Garbage Collection in Java?
* An automatic memory management process in the JVM.
* Identifies and deletes unreferenced objects from the **Heap Memory** to reclaim memory.
* JVM determines unreachable objects using Root Tracing (GC Roots).
* Can suggest GC using `System.gc()`, but execution is not guaranteed immediately.

---

## 💻 Running the Mock Interview Practice Tool

Run the interactive terminal interview practice tool:

```bash
python mock_interview.py
```
