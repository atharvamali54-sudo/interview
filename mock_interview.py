#!/usr/bin/env python3
"""
Interactive Java Mock Interview Practice CLI
Helps candidates practice and self-evaluate Java technical interview questions.
"""

import time

QUESTIONS = [
    {
        "id": 1,
        "question": "What are the 4 fundamental pillars of Object-Oriented Programming (OOP) in Java?",
        "keywords": ["encapsulation", "inheritance", "polymorphism", "abstraction"],
        "ideal_answer": "The four main OOP concepts in Java are:\n"
                        "1. Encapsulation: Binding data and methods into a single class with private variables.\n"
                        "2. Inheritance: Reusing parent class properties in child classes using 'extends'.\n"
                        "3. Polymorphism: Performing a single action in different ways (Overloading & Overriding).\n"
                        "4. Abstraction: Hiding implementation details using Abstract classes and Interfaces."
    },
    {
        "id": 2,
        "question": "What is the difference between '==' operator and '.equals()' method in Java?",
        "keywords": ["reference", "memory", "address", "content", "value"],
        "ideal_answer": "The '==' operator checks reference equality (whether both references point to the exact same memory address).\n"
                        "The '.equals()' method compares the actual content or values inside the objects."
    },
    {
        "id": 3,
        "question": "Why is String immutable in Java?",
        "keywords": ["pool", "constant pool", "security", "thread safe", "thread-safe", "memory", "cannot change"],
        "ideal_answer": "Strings are immutable (cannot be modified after creation) for:\n"
                        "1. Security: Sensitive data like database URLs and passwords cannot be tampered with.\n"
                        "2. Thread Safety: Multiple threads can safely access strings without synchronization.\n"
                        "3. Memory Optimization: Enables the String Constant Pool to save heap memory."
    },
    {
        "id": 4,
        "question": "What is the difference between Interface and Abstract Class in Java?",
        "keywords": ["multiple inheritance", "abstract", "default", "concrete", "implements", "extends"],
        "ideal_answer": "An interface supports multiple inheritance and contains mostly abstract methods (or default/static methods in Java 8+).\n"
                        "An abstract class supports single inheritance and can contain both abstract and concrete methods."
    },
    {
        "id": 5,
        "question": "Explain the difference between final, finally, and finalize in Java.",
        "keywords": ["keyword", "constant", "block", "cleanup", "garbage", "collector"],
        "ideal_answer": "'final' is a keyword to make variables constant, methods un-overridable, or classes un-inheritable.\n"
                        "'finally' is a block attached to try-catch that always executes for cleanup code.\n"
                        "'finalize()' is a method called by the garbage collector before deleting an object."
    }
]

def run_mock_interview():
    print("=" * 65)
    print("      🎯 JAVA MOCK INTERVIEW PRACTICE (INTERNSHALA / TECH ROUND)")
    print("=" * 65)
    print("Welcome! Answer each question in 1-3 sentences.")
    print("Type your answer and press Enter. (Type 'exit' to quit at any time)\n")
    
    total_score = 0
    total_questions = len(QUESTIONS)
    
    for item in QUESTIONS:
        print(f"\n[Question {item['id']}/{total_questions}]:")
        print(f"👉 {item['question']}\n")
        
        user_ans = input("Your Answer: ").strip()
        if user_ans.lower() == "exit":
            print("\nExiting practice session. Keep learning!")
            return
            
        print("\n⏳ Evaluating your answer...")
        time.sleep(1)
        
        # Check matched keywords
        ans_lower = user_ans.lower()
        matched = [k for k in item["keywords"] if k in ans_lower]
        score = min(100, int((len(matched) / max(2, len(item["keywords"]))) * 100))
        total_score += score
        
        if score >= 60:
            print("✅ Great job! Key points were mentioned.")
        else:
            print("⚠️ You missed some key technical terms.")
            
        print(f"Keywords detected: {matched}")
        print("\n⭐ Ideal Answer to speak in the interview:")
        print(item["ideal_answer"])
        print("-" * 65)

    final_avg = total_score // total_questions
    print(f"\n🎉 Practice Finished! Your Average Score: {final_avg}/100")
    if final_avg >= 70:
        print("🌟 Excellent! You are ready for the Java assessment.")
    else:
        print("💡 Review the README.md and Java_Revision_Marathi.md to polish your answers!")

if __name__ == "__main__":
    run_mock_interview()
