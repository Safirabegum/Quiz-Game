# Simple Quiz Game in Python

# Function to ask questions and check answers
def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    # Get the user's answer
    answer = input("Your answer (1/2/3/4): ")
    
    # Check if the answer is correct
    if answer == str(correct_option):
        print("Correct!\n")
        return 1
    else:
        print("Wrong! The correct answer was:", options[correct_option - 1], "\n")
        return 0

# List of quiz questions, options, and correct answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "correct_option": 3
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_option": 2
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["J.K. Rowling", "J.R.R. Tolkien", "George R.R. Martin", "Stephen King"],
        "correct_option": 1
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"],
        "correct_option": 4
    },
]

# Initialize the score
score = 0

# Loop through the questions and ask them
for q in questions:
    score += ask_question(q["question"], q["options"], q["correct_option"])

# Final score
print(f"Your final score is {score}/{len(questions)}")

# Optional: Add a congratulatory message if the score is perfect
if score == len(questions):
    print("Congratulations! You got all questions correct!")
