import time
import threading # which allows your program to run multiple tasks (threads) at the same time.

# Questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used in web development?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. C++"],
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. James Gosling", "D. Bjarne Stroustrup"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    }
]

score = 0
timeout = False  # Flag to track if the time is up

def input_with_timeout(prompt, timeout_duration):
    """Function to take input with a timeout."""
    global timeout #means that we are referring to the timeout variable outside the function. 
    answer = None

    def take_input():
        """Thread function to take user input."""
        nonlocal answer
        answer = input(prompt).strip().upper()

    # Start input thread
    input_thread = threading.Thread(target=take_input)
    input_thread.start()

    # Wait for the input or timeout
    input_thread.join(timeout_duration)

    if input_thread.is_alive():
        timeout = True
        print("\nTime's up! Moving to the next question...\n")
        return None
    return answer

# Start the quiz
print("Welcome to the Quiz Game!")
print("You have 10 seconds to answer each question.\n")

for i, q in enumerate(questions, 1):
    print(f"Q{i}: {q['question']}")
    for option in q["options"]:
        print(option)

    timeout = False  # Reset timeout flag for each question
    answer = input_with_timeout("Enter your answer (A, B, C, or D): ", 10)

    if timeout or answer not in ["A", "B", "C", "D"]:  
        print(f"The correct answer was {q['answer']}.\n")
    elif answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.\n")

print(f"Quiz Over! Your final score: {score}/{len(questions)}")
