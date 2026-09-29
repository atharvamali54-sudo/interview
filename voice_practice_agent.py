#!/usr/bin/env python3
"""
Voice-Enabled Java Mock Interview Practice Agent
Designed for students to practice listening, speaking, and revising Java interview questions aloud.
"""

import os
import sys
import time
import tempfile
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import pyttsx3
import speech_recognition as sr

# Optional Gemini Integration
try:
    from google import genai
    gemini_client = genai.Client() if os.environ.get("GEMINI_API_KEY") else None
except Exception:
    gemini_client = None

# Built-in High-Yield Java Knowledge Base for instant offline voice answers
JAVA_KB = {
    "oops": (
        "Object Oriented Programming has four core pillars: "
        "Encapsulation binds data and methods together with private variables. "
        "Inheritance allows child classes to inherit parent properties. "
        "Polymorphism allows one method to take multiple forms through overloading and overriding. "
        "Abstraction hides implementation details using abstract classes and interfaces."
    ),
    "encapsulation": (
        "Encapsulation is wrapping data and code into a single unit like a class. "
        "We declare class variables as private and provide public getters and setters to protect data."
    ),
    "inheritance": (
        "Inheritance is a mechanism where a new class derives properties and behaviors from an existing class using the extends keyword. "
        "It promotes code reusability."
    ),
    "polymorphism": (
        "Polymorphism means many forms. There are two types: "
        "Compile time polymorphism, achieved via Method Overloading, and "
        "Runtime polymorphism, achieved via Method Overriding."
    ),
    "abstraction": (
        "Abstraction means showing only essential features and hiding background details. "
        "In Java, abstraction is achieved using Abstract Classes and Interfaces."
    ),
    "equals": (
        "The double equals operator compares object memory references. "
        "The dot equals method compares the actual values or contents inside the objects."
    ),
    "string": (
        "In Java, String is immutable, meaning once created, its value cannot be changed. "
        "This provides thread safety, security for sensitive data, and enables the String Constant Pool."
    ),
    "builder": (
        "String is immutable. StringBuilder is mutable, fast, but not thread-safe. "
        "StringBuffer is mutable and thread-safe because its methods are synchronized."
    ),
    "interface": (
        "An interface supports multiple inheritance and has abstract methods by default. "
        "An abstract class supports single inheritance and can contain both abstract and concrete methods."
    ),
    "hashmap": (
        "HashMap stores data in key-value pairs using hashing. "
        "It uses hashCode to find bucket index. In Java 8, if a bucket has more than 8 elements, "
        "it converts from a linked list to a balanced red-black tree for faster lookup."
    ),
    "finally": (
        "Final is a keyword for constants. "
        "Finally is a block that always executes with try-catch for cleanup. "
        "Finalize is a method called by the garbage collector before deleting an object."
    ),
    "exception": (
        "Exceptions are divided into Checked exceptions, checked at compile time like IOException, "
        "and Unchecked exceptions, which occur at runtime like NullPointerException and ArithmeticException."
    )
}

# Setup Text-To-Speech
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 160)

def speak(text):
    """Prints and speaks the given text aloud."""
    print(f"\n🔊 [AI Assistant]: {text}\n")
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"(Speech error: {e})")

def record_audio(duration=5, sample_rate=44100):
    """Records audio from microphone using sounddevice."""
    print(f"\n🎤 [माइक चालू आहे] बोला ({duration} सेकंद)...")
    try:
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()
        
        # Save to temporary WAV file
        temp_wav = os.path.join(tempfile.gettempdir(), f"mic_rec_{int(time.time())}.wav")
        write(temp_wav, sample_rate, recording)
        return temp_wav
    except Exception as e:
        print(f"❌ Microphone recording error: {e}")
        return None

def transcribe_audio(wav_path):
    """Converts recorded WAV audio to text using SpeechRecognition."""
    if not wav_path or not os.path.exists(wav_path):
        return ""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            print(f"📝 [Transcribed Voice]: \"{text}\"")
            return text
    except sr.UnknownValueError:
        print("⚠️ आवाज नीट समजला नाही. कृपया पुन्हा स्पष्ट बोला.")
        return ""
    except Exception as e:
        print(f"⚠️ Speech Recognition error: {e}")
        return ""
    finally:
        try:
            os.remove(wav_path)
        except Exception:
            pass

def find_answer(query):
    """Finds technical Java answer from local KB or Gemini."""
    q_lower = query.lower()
    
    # 1. Local KB match
    for key, ans in JAVA_KB.items():
        if key in q_lower:
            return ans
            
    if "oops" in q_lower or "object oriented" in q_lower:
        return JAVA_KB["oops"]
    if "==" in q_lower or "equals" in q_lower:
        return JAVA_KB["equals"]
    if "immutable" in q_lower or "string" in q_lower:
        return JAVA_KB["string"]

    # 2. Gemini Fallback if available
    if gemini_client:
        try:
            prompt = f"Answer this Java interview question concisely in 2-3 clear sentences for spoken interview: {query}"
            resp = gemini_client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            return resp.text.strip()
        except Exception:
            pass

    return (
        "In Java, ensure you explain the concept with definition, core advantages, "
        "and a simple real-world example to answer clearly."
    )

def mode_voice_qa():
    """Mode 1: Speak a question, AI answers in voice."""
    speak("Voice Practice Mode is active. Ask any Java question to hear the ideal answer.")
    while True:
        print("\nOptions:")
        print("1. Press [Enter] to record your voice question (5 seconds)")
        print("2. Type your question manually")
        print("3. Back to main menu (type 'b')")
        choice = input("Select: ").strip()
        
        if choice.lower() == 'b':
            break
        elif choice == '2':
            q = input("\nEnter your Java question: ").strip()
            if q:
                ans = find_answer(q)
                speak(ans)
        else:
            wav_file = record_audio(duration=5)
            if wav_file:
                query = transcribe_audio(wav_file)
                if query:
                    ans = find_answer(query)
                    speak(ans)
                else:
                    speak("Could not catch your voice. Please try again or type.")

def mode_mock_interviewer():
    """Mode 2: AI asks question in voice, you answer, AI gives feedback."""
    questions = [
        ("What are the core OOPs concepts in Java?", "oops"),
        ("What is the difference between equals and double equals in Java?", "equals"),
        ("Why is String immutable in Java?", "string"),
        ("What is the difference between interface and abstract class?", "interface"),
        ("Explain final, finally, and finalize in Java.", "finally")
    ]
    
    speak("Starting Mock Interview Practice. I will ask questions aloud.")
    for idx, (q, key) in enumerate(questions, 1):
        speak(f"Question number {idx}: {q}")
        print("\n1. Press [Enter] to speak your answer (8 seconds)")
        print("2. Type your answer")
        choice = input("Select: ").strip()
        
        user_answer = ""
        if choice == '2':
            user_answer = input("Your answer: ").strip()
        else:
            wav_file = record_audio(duration=8)
            if wav_file:
                user_answer = transcribe_audio(wav_file)
                
        print(f"\n👉 Your answer was: {user_answer if user_answer else '(No input recorded)'}")
        speak("Here is the model answer to speak in your interview:")
        speak(JAVA_KB[key])
        time.sleep(1)

    speak("Mock interview practice finished. Great work!")

def main():
    while True:
        print("\n" + "="*55)
        print("   🎯 JAVA VOICE MOCK INTERVIEW PRACTICE ASSISTANT")
        print("="*55)
        print("1. Voice Q&A Mode (तुम्ही प्रश्न बोला -> AI आवाजात उत्तर देईल)")
        print("2. Mock Interview Mode (AI प्रश्न विचारेल -> तुम्ही उत्तर द्या)")
        print("3. Exit")
        choice = input("Choose (1/2/3): ").strip()
        
        if choice == '1':
            mode_voice_qa()
        elif choice == '2':
            mode_mock_interviewer()
        elif choice == '3':
            print("Exiting. Best of luck for your interview preparation!")
            break

if __name__ == "__main__":
    main()
